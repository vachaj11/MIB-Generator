"""This module serves the purpose of parsing C files containing basic information about the various packet to be included in the MIB database."""
import parsing.par_methods as parm

types = {"uint8_t", "uint16_t", "uint32_t", "uint64_t", "char", "unsigned int"}
typea = types.union({"struct"})


def str_parse(stri):
    """Parse the given string into blocks of "top-level" C-structures."""
    strc = parm.erase_text(stri)
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
        x = parm.clean(cont, {"//", "\n", "/*", "*/"})
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
                # this ugly thing takes care of trailing commas
                if not lis:
                    lis.append(i)
                else:
                    block = parm.clean(body[lis[-1] + 1 : i], {"\n", "\t"}).replace(
                        " ", ""
                    )
                    if len(block) > 2:
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
