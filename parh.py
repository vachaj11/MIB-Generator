"""This module serves the purpose of parsing C header files containing information about the structure of packets."""
import json5

types = {"uint8_t", "uint16_t", "uint32_t", "uint64_t", "char", "unsigned int"}


def clean(stri, tokens):
    """Replace tokens with spaces."""
    c = stri
    for i in tokens:
        c = c.replace(i, " " * len(i))
    return c


def erase_text(stri):
    """Erase all text inside quatation marks in the given string."""
    mod = 0  # 0 for no quation, 1 for ' and 2 for "
    new = stri
    for i in range(len(stri)):
        if stri[i] == '"' and mod != 2:
            if mod == 0:
                mod = 1
            else:
                mod = 0
        elif stri[i] == "'" and mod != 1:
            if mod == 0:
                mod = 2
            else:
                mod = 0
        elif mod != 0:
            new = new[:i] + " " + new[i + 1 :]
    return new


def line_index(stri):
    """Give list of indexes of line starts of the given string."""
    starts = []
    for i in range(len(stri)):
        if stri[i] == "\n":
            starts.append(i + 1)
    return starts


def split_comment(stri):
    """Split the given string into a section with C comments and a section without them."""
    mod = (
        0  # 0 for normal content, 1 for '...', 2 for "...", 3 for /* ...*/ and 4 for //
    )
    comm = ""
    cont = ""
    start = 0
    sections = []
    for i in range(
        len(stri)
    ):  # iterates through the string and marks different sections of it
        x = stri[i]
        xy = stri[i : i + 2]
        if x == '"' and mod == 2:
            mod = 0
        elif x == '"' and mod == 0:
            mod = 2
        elif x == "'" and mod == 1:
            mod = 0
        elif x == "'" and mod == 0:
            mod = 1
        elif xy == "/*" and mod == 0:
            mod = 3
            sections.append([start, i + 1])
            start = i + 2
        elif xy == "*/" and mod == 3:
            mod = 0
            sections.append([start, i - 1])
            start = i
        elif xy == "//" and mod == 0:
            mod = 4
            sections.append([start, i + 1])
            start = i + 2
        elif x == "\n" and mod == 4:
            mod = 0
            sections.append([start, i - 1])
            start = i

    if sections[-1][-1] != len(stri) - 1:
        sections.append([start, len(stri) - 1])
    switch = False  # keeps track of whether a given section is a content or a comment
    for i in sections:
        cut = stri[i[0] : i[1] + 1]
        if not switch:
            cont = cont + cut
            # comm = comm + " " * len(cut)
            if cut[:1] == "\n":  # horrible bodge which will come back to haunt me
                comm = comm + cut[:1] + " " * (len(cut) - 3) + cut[1:][-2:]
            else:
                comm = comm + cut[:2] + " " * (len(cut) - 4) + cut[2:][-2:]
        else:
            cont = cont + " " * len(cut)
            comm = comm + cut
        switch = not switch
    return cont, comm


def str_parse(stri):
    """Parse the given string into blocks of "top-level" C-structures."""
    strc = erase_text(stri)
    depth = 0
    structures = []
    start = 0
    typ = ""
    for i in range(len(stri)):
        if strc[i] not in {"#", "e", "s", ";", "\n", "}", "{", ")", "("}:
            pass
        elif strc[i : i + 7] == "#define" and depth == 0:
            start = i
            depth = 1
            typ = "define"
        elif strc[i : i + 4] == "enum" and depth == 0:
            start = i
            depth = 1
            typ = "enum"
        elif strc[i : i + 6] == "struct" and depth == 0:
            start = i
            depth = 1
            typ = "struct"
        elif strc[i : i + 6] == "extern" and depth == 0:
            start = i
            depth = 1
            typ = "extern"
        elif strc[i] == "\n" and depth == 1 and typ == "define":
            depth = 0
            structures.append(define(typ, start, i - 1, stri[start:i]))
        elif strc[i] == ";" and depth == 1 and typ in {"extern", "struct", "enum"}:
            depth = 0
            if typ == "extern":
                structures.append(extern(typ, start, i - 1, stri[start:i]))
            elif typ == "enum":
                structures.append(enum(typ, start, i - 1, stri[start:i]))
            elif typ == "struct":
                structures.append(struct(typ, start, i - 1, stri[start:i]))
        elif strc[i] in {"}", ")"}:
            depth -= 1
        elif strc[i] in {"{", "("}:
            depth += 1
    return structures


def str_parse_r(offset, stri):
    """Parse the given string into blocks of C-structures. But this time "second-order" strings are expected and the parsing is recursive."""
    strc = erase_text(stri)
    depth = 0
    structures = []
    start = 0
    typ = ""
    for i in range(len(stri)):
        if strc[i] not in {"e", "s", ";", "\n", "}", "{", ")", "(", "u", "c"}:
            pass
        elif strc[i : i + 4] == "enum" and depth == 0:
            start = i
            depth = 1
            typ = "enum"
        elif strc[i : i + 6] == "struct" and depth == 0:
            start = i
            depth = 1
            typ = "struct"
        elif strc[i:].startswith(tuple(types)) and depth == 0:
            start = i
            depth = 1
            for l in types:
                if strc[i:].startswith(l):
                    typ = l
        elif strc[i] == ";" and depth == 1:
            depth = 0
            if typ == "enum":
                structures.append(
                    enum_r(typ, offset + start, offset + i - 1, stri[start:i])
                )
            elif typ == "struct":
                structures.append(
                    struct_r(typ, offset + start, offset + i - 1, stri[start:i])
                )
            else:
                structures.append(
                    misc_r(typ, offset + start, offset + i - 1, stri[start:i])
                )
        elif strc[i] in {"}", ")"}:
            depth -= 1
        elif strc[i] in {"{", "("}:
            depth += 1
    return structures


class structure:
    """class of first order header structures/object"""

    def __init__(self, typ, inds, inde, cont):
        self.type = typ
        self.start = inds
        self.end = inde
        self.text = cont
        self.comment = []


class enum(structure):
    """class of enum structure"""

    def __init__(self, typ, inds, inde, cont):
        structure.__init__(self, typ, inds, inde, cont)
        self.name, self.entries = self.ele_parse(cont)

    def ele_parse(self, cont):
        """Parse enum into its syntactic/semantic components."""
        x = clean(cont, {"enum", "//", "\n", "/*", "*/"})
        x = x.replace(" ", "")
        brack = 0
        comma = []
        for i in range(len(x)):
            if x[i] == "{":
                brack = i
            elif x[i] == ",":
                comma.append(i)
        name = x[:brack]
        comma = [brack] + comma + [len(x) - 1]
        elem = []
        for i in range(len(comma) - 1):
            elem.append(x[comma[i] + 1 : comma[i + 1]])
        numb = []
        keys = []
        for i in elem:
            if "=" in i:
                position = i.find("=")
                try:
                    numb.append(int(i[position + 1 :]))
                except:
                    numb.append(int(i[position + 1 :]))
                keys.append(i[:position])
            else:
                if len(numb) != 0:
                    numb.append(numb[-1] + 1)
                else:
                    numb.append(0)
                keys.append(i)
        return name, dict(zip(keys, numb))


class define(structure):
    """class of #define makro"""

    def __init__(self, typ, inds, inde, cont):
        structure.__init__(self, typ, inds, inde, cont)
        self.name, self.expression = self.def_parse(cont)

    def def_parse(self, cont):
        """Parse #define into its syntactic/semantic components."""
        x = clean(cont, {"//", "\n", "/*", "*/"})
        x = x[8:]
        if " " in x:
            ind = x.find(" ")
            return x[:ind], x[ind + 1 :]
        else:
            return x, ""


class extern(structure):
    """class of external declaration of a constant"""

    def __init__(self, typ, inds, inde, cont):
        structure.__init__(self, typ, inds, inde, cont)
        self.flav, self.name, self.array = self.ext_parse(cont)

    def ext_parse(self, cont):
        """Parse extern into its syntactic/semantic components."""
        x = clean(cont, {"//", "\n", "/*", "*/"})
        x = x[13:]
        ind = x.find(" ")
        part_1 = x[:ind]
        x = x[ind + 1 :]
        if " " in x:
            ind = x.find(" ")
            part_2 = " " + x[:ind]
            x = x[ind + 1 :]
        else:
            part_2 = ""
        if "[" in x and "]" in x:
            ind = x.find("[")
            part_3 = x[:ind]
            inde = x.find("]")
            part_4 = x[ind + 1 : inde]
        else:
            part_3 = x
            part_4 = "-1"
        return part_1 + part_2, part_3, part_4


class struct(structure):
    """class of declaration of a C structure"""

    def __init__(self, typ, inds, inde, cont):
        structure.__init__(self, typ, inds, inde, cont)
        self.name, self.packed, self.elements = self.stc_parse(cont)

    def stc_parse(self, cont):
        """Parse struct into its syntactic/semantic components."""
        x = clean(cont, {"//", "\n", "/*", "*/"})
        x = x[7:]
        ind = x.find("{")
        head = x[:ind]
        body = x[ind + 1 : -1]
        if "PACKED" in head:
            packed = True
            name = head[7:].replace(" ", "")
        else:
            packed = False
            name = head.replace(" ", "")
        entries = str_parse_r(ind + 8 + self.start, body)
        return name, packed, entries


class struct_r(structure):
    """class of a reference to a C structure"""

    def __init__(self, typ, inds, inde, cont):
        structure.__init__(self, typ, inds, inde, cont)
        self.name, self.form, self.array = self.str_parse(cont)

    def str_parse(self, cont):
        """Parse the reference to its syntactic/semantic components."""
        if "{" not in cont or "}" not in cont:
            x = cont[7:]
            ind = x.find(" ")
            form = x[:ind]
            rest = x[ind + 1 :]
        else:
            ind = cont.rfind("}")
            form = struct("struct", self.start, self.start + ind + 1, cont[: ind + 1])
            rest = cont[ind + 1 :]
        if "[" in rest and "]" in rest:
            ind = rest.find("[")
            inde = rest.find("]")
            array = rest[ind + 1 : inde]
            rest = rest[:ind] + rest[inde + 1 :]
        else:
            array = "-1"
        return rest.replace(" ", ""), form, array


class enum_r(structure):
    """class of a reference to an enum"""

    def __init__(self, typ, inds, inde, cont):
        structure.__init__(self, typ, inds, inde, cont)
        self.name, self.form, self.bites, self.array = self.enr_parse(cont)

    def enr_parse(self, cont):
        """Parse the reference to its syntactic/semantic components."""
        if "{" not in cont or "}" not in cont:
            x = cont[5:]
            ind = x.find(" ")
            form = x[:ind]
            rest = x[ind + 1 :]
        else:
            ind = cont.rfind("}")
            form = enum("enum", self.start, self.start + ind + 1, cont[: ind + 1])
            rest = cont[ind + 1 :]
        if "[" in rest and "]" in rest:
            ind = rest.find("[")
            inde = rest.find("]")
            array = rest[ind + 1 : inde]
            rest = rest[:ind] + rest[inde + 1 :]
        else:
            array = "-1"
        if ":" in rest:
            ind = rest.find(":")
            try:
                byte = int(rest[ind + 1 :].replace(" ", ""))
                rest = rest[:ind]
            except:
                byte = -1
        else:
            byte = -1
        return rest.replace(" ", ""), form, byte, array


class misc_r(structure):
    """class of a declaration of a constant"""

    def __init__(self, typ, inds, inde, cont):
        structure.__init__(self, typ, inds, inde, cont)
        self.name, self.bites, self.array = self.mir_parse(cont)

    def mir_parse(self, cont):
        """Parse the declaration into its syntactic/semantic components."""
        rest = cont[len(self.type) + 1 :]
        if "[" in rest and "]" in rest:
            ind = rest.find("[")
            inde = rest.find("]")
            array = rest[ind + 1 : inde]
            rest = rest[:ind] + rest[inde + 1 :]
        else:
            array = "-1"
        if ":" in rest:
            ind = rest.find(":")
            try:
                byte = int(rest[ind + 1 :].replace(" ", ""))
                rest = rest[:ind]
            except:
                byte = -1
        else:
            byte = -1
        return rest.replace(" ", ""), byte, array


def com_parse(comm):
    """Parse the comments in the string into blocks corresponding to singular comments."""
    depth = 0
    start = 0
    blocks = []
    for i in range(len(comm)):
        if comm[i : i + 3] == "/*{" and depth == 0:
            start = i + 2
            depth = 1
        elif comm[i : i + 3] == "}*/" and depth == 1:
            blocks.append(comment(start, i, comm[start : i + 1]))
            depth = 0
        elif comm[i : i + 2] == "//" and depth == 0:
            depth = 2
        elif comm[i] == "\n" and depth == 2:
            depth = 0
    return blocks


class comment:
    """class of an occurence of a comment in the file"""

    def __init__(self, start, end, text):
        self.text = text
        self.start = start
        self.end = end
        try:
            self.entries = json5.loads(text)
        except:
            print("Error at" + self.text)


class file:
    """class resresenting the file being analysed, its structure, etc..."""

    def __init__(self, stri):
        self.text = stri
        self.max_position = len(stri)
        self.lines = line_index(stri)
        self.text_o, self.text_c = split_comment(stri)
        self.structures = str_parse(self.text_o)
        self.comments = com_parse(self.text_c)
        self.link = self.linker()

    def linker(self):
        """Link each comment to a corresponding C-object in the file"""
        pairs = []
        for i in self.comments:
            ind = i.start
            elem = {}
            minim = 50000
            for l in self.structures:
                if l.start <= ind <= l.end:
                    if l.type != "enum":  # very ugly bodge again
                        for k in l.elements:
                            if ind - k.end >= 0 and ind - k.end <= minim:
                                elem = k
                                minim = ind - k.end
                    else:
                        elem = l
                        minim = 49999

                    break
            if minim == 50000:
                for l in self.structures:
                    if l.start - ind >= 0 and l.start - ind <= minim:
                        elem = l
                        minim = l.start - ind
            pairs.append([i, elem])
            elem.comment.append(i)
        return pairs


def main(name="/home/vachaj11/Documents/MIB/start/src/PUS_TmDefs.h"):
    """Run it all."""
    try:
        fil = open(name, "r")
        c = fil.read()
        fil.close()
    except:
        c = ""
    x = file(c)
    x.path = name
    return x
