"""This module serves the purpose of parsing C header files containing information about the structure of packets."""
import parsing.par_methods as parm

types = {"uint8_t", "uint16_t", "uint32_t", "uint64_t", "char", "unsigned int"}


def str_parse(stri):
    """Parse the given string into blocks of "top-level" C-structures."""
    strc = parm.erase_text(stri)
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
    strc = parm.erase_text(stri)
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
        x = parm.clean(cont, {"enum", "//", "\n", "/*", "*/"})
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
        # takes care of trailing commas
        if comma[-1] - comma[-2] < 2:
            comma.pop(-1)
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
        x = parm.clean(cont, {"//", "\n", "/*", "*/"})
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
        x = parm.clean(cont, {"//", "\n", "/*", "*/"})
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
        x = parm.clean(cont, {"//", "\n", "/*", "*/"})
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
            if ind > 0:
                form = x[:ind]
                rest = x[ind + 1 :]
            else:
                if "[" in x:
                    indb = x.find("[")
                    form = x[:indb]
                    rest = x[indb:]
                else:
                    form = x
                    rest = ""
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
