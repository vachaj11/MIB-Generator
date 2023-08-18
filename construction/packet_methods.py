"""This module holds methods used for formatting parsed data into packet characteristics."""
import parsing.load as load
import data.longdata as longdata
from copy import copy


def apidnum(name):
    """Find the value of apid from evaluation of references, etc.
    I'm not following the direct logic of C here, because there seems to be some missing link.
    """
    num = load.enumerations[name]
    lis = next((x for x in load.TmC.structures if x.name == "apidNum"), None)
    link = {}
    for i in lis.elements:
        link[str(load.enumerations[i.position[1:-1]])] = int(i.value)
    return link[str(num)]


def evalu(string):
    """Try evaluating the given expression using all known substitutions, macros, etc."""
    try:
        x = int(string)
    except:
        if string in load.enumerations.keys():
            x = load.enumerations[string]
        else:
            try:
                x = eval(string, load.enumerations)
            except:
                x = -1
                print("Warn.:\tWasn't able to find the numerical value of " + string)
    return x


def getptcpcf(entry, size):
    """Get ptc and pcf values from the size and nature of the given entry."""
    try:
        typ = entry.comment[-1].entries["type"]
    except:
        typ = "-1"
    if typ.startswith("CUCTIME"):
        ptc = 9
        pfc = longdata.time_pfc.index([int(typ[7]), int(typ[9])])
    elif entry.array != "-1":
        ptc = 7
        pfc = int(size / 8)
    elif entry.type.startswith("uint"):
        ptc = 3
        pfc = longdata.uint_pfc.index(size)
    elif entry.type == "enum":
        ptc = 2
        pfc = size
    else:
        ptc = 3
        pfc = 16
    return ptc, pfc


def categfromptc(ptc):
    """Get category from ptc value of the entry."""
    if ptc in {2, 3, 6, 7, 9, 10}:
        categ = "N"
    elif ptc == 8:
        categ = "T"
    else:
        categ = "S"
    return categ


def header_search(typ):
    """Search for corresponding header structures of the packet based on information in the comments."""
    hstruct = []
    for i in load.TmH.structures:
        if i.type == "struct" and i.comment:
            uni = {}
            for l in i.comment:
                uni.update(l.entries)
            if "pack_type" in uni.keys() and uni["pack_type"] == typ:
                hstruct.append(i)
    if typ in load.enumerations.keys() and not hstruct:
        hstruct.append(load.enumerations[typ])
    if not hstruct:
        print(
            "Warn.:\tWasn't able to establish the link of packet "
            + typ
            + " to any header structure."
        )
    return hstruct


def h_analysis(h_struct):
    """Make a list of all individual (all structs unpacked) entries in the header of the packet."""
    entries = []
    if not (type(h_struct) is int or type(h_struct) is None):
        for i in h_struct.elements:
            if i.type not in {"enum", "struct"}:
                # this is insanely ugly, but at least it shouldn't create any confusion
                if i.comment and "vpd" in i.comment[-1].entries.keys():
                    i.is_vpd = i.comment[-1].entries["vpd"]
                else:
                    i.is_vpd = ""
                entries.append(i)
            elif i.type == "struct":
                occurences = 1
                from_struct = []
                if evalu(i.array) > 0:
                    occurences = evalu(i.array)
                if i.comment and "vpd" in i.comment[-1].entries.keys():
                    occurences = 1
                    vpd = True
                else:
                    vpd = False
                for k in range(occurences):
                    if type(i.form) is str:
                        name = i.form
                        for l in load.TmH.structures + load.TcTmH.structures:
                            if l.name == name:
                                from_struct = [copy(x) for x in h_analysis(l)]
                    else:
                        from_struct = [copy(x) for x in h_analysis(i.form)]
                if vpd:
                    for k in from_struct:
                        k.is_vpd = i.comment[-1].entries["vpd"]
                entries = entries + from_struct

    return entries


def var_get(entries):
    "Extract variable parameters from list of all parameters."
    var = []
    for i in range(len(entries)):
        com = entries[i].comment
        if entries[i].is_vpd:
            var.append(i)
    return var


def count_size(entries):
    """Counts bit size of the packet and bit position of entries within it."""
    size_bites = 0
    positions = []
    sizes = longdata.sizes
    for i in entries:
        positions.append(size_bites)
        if i.bites != -1:
            size_bites += i.bites
        else:
            array = 1
            if evalu(i.array) != -1:
                array = evalu(i.array)
            try:
                size_bites += array * (sizes[i.type])
            except:
                print("Unknown size of type " + i.type)
    return int(size_bites / 8), positions + [size_bites]


def pi_sid(entries, positions):
    "Extract position of additional identification field from packet entries."
    start = None
    width = 0
    for i in range(len(entries)):
        if entries[i].name == "sid":
            start = int(positions[i] / 8)
            width = positions[i + 1] - positions[i]
    return start, width
