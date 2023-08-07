import json5

types = {"uint8_t", "uint16_t", "uint32_t", "uint64_t", "char", "unsigned int"}
typea = types.union({"struct"})


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
        if strc[i] not in {"c", "s", "u", ";", "}", "{", ")", "("}:
            pass
        elif depth == 0 and (
            (strc[i : i + 5] == "const" and strc[i + 7 :].startswith(tuple(typea)))
            or strc[i:].startswith(tuple(typea))
        ):
            start = i
            depth = 1
            for l in typea:
                if strc[i:].startswith(l) or (
                    strc[: i + 5] == "const" and strc[i:].startswith(l)
                ):
                    typ = l
        elif strc[i] == ";" and depth == 1:
            depth = 0
            if typ == "struct":
                structures.append(struct(typ, start, i - 1, stri[start:i]))
            else:
                structures.append(miscal(typ, start, i - 1, stri[start:i]))
        elif strc[i] in {"}", ")"}:
            depth -= 1
        elif strc[i] in {"{", "("}:
            depth += 1
    return structures


class instance_og:
    """class of general C structures/object"""
    def __init__(self, typ, inds, inde, cont):
        self.type = typ
        self.start = inds
        self.end = inde
        self.text = cont
        self.comment = []


class instance(instance_og):
    """class of first order C structures/object""" 
    def __init__(self, typ, inds, inde, cont):
        instance_og.__init__(self, typ, inds, inde, cont)
        self.name, self.array, self.elements = self.str_parse(cont)

    def str_parse(self, cont):
        """Parse some general information about the object"""
        x = clean(cont, {"//", "\n", "/*", "*/"})
        if x[:6] == "const":
            x = x[7:]

        ind = x.find("=")
        head = x[len(self.type) + 1 : ind]
        body = x[ind + 1 :]
        if "[" in head and "]" in head:
            inds = head.find("[")
            inde = head.find("]")
            array = head[inds + 1 : inde]
            head = head[:inds] + head[inde + 1 :]
        else:
            array = "-1"
        depth = 0
        lis = []
        for i in range(len(body)):
            if body[i] == "{":
                depth += 1
            elif body[i] == "}":
                depth -= 1
            if (body[i] in {",", "{"} and depth == 1) or (
                body[i] == "}" and depth == 0
            ):
                lis.append(i)
        elem = []
        for i in range(len(lis) - 1):
            start = self.start + ind + lis[i] + 2
            end = self.start + ind + lis[i + 1]
            text = body[lis[i] + 1 : lis[i + 1]]
            if self.type == "struct":
                elem.append(struct_r(self.type, start, end, text))
            else:
                elem.append(misc_r(self.type, start, end, text))
        return head, array, elem


class struct(instance):
    """class of an instance of an array of structs"""
    def __init__(self, typ, inds, inde, cont):
        instance.__init__(self, typ, inds, inde, cont)
        self.flav, self.name = self.add_parse(self.name)
        if self.array != "-1":
            self.reposition()

    def add_parse(self, name):
        """Correct information about the object's name and type."""
        inds = name.find(" ")
        nname = name[inds + 1 :].replace(" ", "")
        flav = name[:inds].replace(" ", "")
        for i in self.elements:
            i.name = flav
        return flav, nname

    def reposition(self):
        """Use classic ordering if no specific position of each element of a structure is declared"""
        for i in range(len(self.elements)):
            if self.elements[i].position == "-1":
                self.elements[i].position = str(i)


class miscal(instance):
    """class of an instance of an array of constants"""
    def __init__(self, typ, inds, inde, cont):
        instance.__init__(self, typ, inds, inde, cont)
        self.name = self.add_parse(self.name)
        if (
            self.array != "-1"
        ):  # this check doesn't make sense really because earlier I've assumed that we are given an array
            self.reposition()

    def add_parse(self, name):
        """Correct information about the object's name and type."""
        nname = name.replace(" ", "")
        for i in self.elements:
            i.flav = nname
        return nname

    def reposition(self):
        """Use classic ordering if no specific position of each element of a structure is declared"""
        for i in range(len(self.elements)):
            if self.elements[i].position == "-1":
                self.elements[i].position = str(i)


class struct_r(instance_og):
    """class of a singular instance of struct (within array)"""
    def __init__(self, typ, inds, inde, cont):
        instance_og.__init__(self, typ, inds, inde, cont)
        self.position, self.entries = self.srr_parse(cont)

    def srr_parse(self, cont):
        """Parse the struct into its entries."""
        if cont.find("=") < cont.find("{"):
            ind = cont.find("=")
            position = cont[:ind].replace(" ", "")
            cont = cont[ind + 1 :]
        else:
            position = "-1"
        depth = 0
        lis = []
        for i in range(len(cont)):
            if cont[i] == "{":
                depth += 1
            elif cont[i] == "}":
                depth -= 1
            if (cont[i] in {",", "{"} and depth == 1) or (
                cont[i] == "}" and depth == 0
            ):
                lis.append(i)
        elem = []
        for i in range(len(lis) - 1):
            elem.append(cont[lis[i] + 1 : lis[i + 1]])
        entr = {}
        for i in elem:
            ind = i.find("=")
            key = i[:ind].replace(" ", "")
            value = i[ind + 1 :].replace(" ", "")
            entr[key] = value
        return position, entr


class misc_r(instance_og):
    """class of a singular instance of a constant (within array)"""
    def __init__(self, typ, inds, inde, cont):
        instance_og.__init__(self, typ, inds, inde, cont)
        self.position, self.value = self.mis_parse(cont)

    def mis_parse(self, cont):
        """Parse the information about the constant"""
        if "=" in cont:
            ind = cont.find("=")
            position = cont[:ind].replace(" ", "")
            value = cont[ind + 1 :].replace(" ", "")
        else:
            position = "-1"
            value = cont.replace(" ", "")
        return position, value


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
            print("Error at"+self.text)


class file:
    """class representing the file being analysed, its structure, etc..."""
    def __init__(self, stri):
        self.text = stri
        self.max_position = len(stri)
        self.lines = line_index(stri)
        self.text_o, self.text_c = split_comment(stri)
        self.structures = str_parse(self.text_o)
        self.comments = com_parse(self.text_c)
        self.link = self.linker()

    def linker(self):
        """Link each comment to a corresponding C-object in the file."""
        pairs = []
        for i in self.comments:
            ind = i.start
            elem = {}
            minim = 50000
            for l in self.structures:
                if l.start <= ind <= l.end:
                    for k in l.elements:
                        if l.type != "enum":  # very ugly bodge again
                            if ind - k.start >= 0 and ind - k.start <= minim:
                                elem = k
                                minim = ind - k.start
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


def main(name="/home/vachaj11/Documents/MIB/start/src/PUS_TmDefs.c"):
    """Run it all."""
    try:
        fil = open(name, "r")
        c = fil.read()
        fil.close()
    except:
        c = ""
    return file(c)
