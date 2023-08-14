"""This module holds methods used for formatting parsed data into packet characteristics."""
import load, longdata

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
            x = -1
            print("Warn.:\tWasn't able to find the numerical value of " + string)
    return x


def getptcpcf(entry, size):
    """Get ptc and pcf values from the size and nature of the given entry."""
    try:
        typ = entry.comment[-1].entries["type"]
    except:
        typ = "-1"
    if typ == "CUCTIME4_3":
        ptc = 9
        pfc = 18
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
    if typ in load.enumerations.keys():
        hstruct.append(load.enumerations[typ])
    if not hstruct:
        print("Warn.:\tWasn't able to establish the link of packet "+typ+" to any header structure.")
    return hstruct

def h_analysis(h_struct):
    """Make a list of all individual (all structs unpacked) entries in the header of the packet."""
    entries = []
    if not (type(h_struct) is int or type(h_struct) is None):
        for i in h_struct.elements:
            if i.type not in {"enum", "struct"}:
                entries.append(i)
            elif i.type == "struct":
                occurences = 1
                if evalu(i.array) > 0:
                    occurences = evalu(i.array)
                for k in range(occurences):
                    if type(i.form) is str:
                        name = i.form
                        for l in load.TmH.structures + load.TcTmH.structures:
                            if l.name == name:
                                entries = entries + h_analysis(l)
                    else:
                        entries = entries + h_analysis(i.form)
    return entries
    
def var_get(entries):
    "Extract variable parameters from list of all parameters."
    var = []
    for i in range(len(entries)):
        com = entries[i].comment
        if com and "var" in com[-1].entries.keys():
            var.append(i)
    return var

def count_size(entries):
    """Counts bit size of the packet header and bit position of entries within it."""
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

