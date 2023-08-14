"""This module takes care of creating a representation of packets from parsed C-files and extracting entries for MIB databases."""
import load, longdata


def apidnum(num):
    """Find the value of apid from evaluation of references, etc.
    I'm not following the direct logic of C here, because there seems to be some missing link.
    """
    lis = next((x for x in load.c_file.structures if x.name == "apidNum"), None)
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


class TM_packet:
    """class representing each TM packet type and its properties"""

    def __init__(self, structure):
        self.structure = structure
        self.h_structure = self.header_search(structure.entries[".type"])
        self.entries = self.h_analysis(self.h_structure)
        self.size, self.positions = self.count_size()
        self.pid = self.pid_dictionary()
        self.pic = self.pic_dictionary()
        self.tpcf = self.tpcf_dictionary()
        self.pcf = self.pcf_listdict()
        self.plf = self.plf_listdict()
        self.cur = self.cur_listdict()

    def pid_dictionary(self):
        """Define elements for entry in pid table."""
        diction = {}
        diction["PID_TYPE"] = evalu(self.structure.entries[".serviceType"])
        diction["PID_STYPE"] = evalu(self.structure.entries[".serviceSubType"])
        diction["PID_APID"] = apidnum(
            load.enumerations[self.structure.entries[".apid"]]
        )
        # diction["PID_PI1_VAL"] =
        # diction["PID_PI_VAL"] =
        try:  # tired bodge
            diction["PID_SPID"] = self.structure.comment[-1].entries["num_id"]
            diction["PID_DESCR"] = self.structure.comment[-1].entries["desc"]
        except:
            diction["PID_SPID"] = ""
            diction["PID_DESCR"] = ""
            print(
                "Warn.:\tNot enough information specified for the packet: "
                + self.structure.entries[".type"]
            )
        # diction["PID_UNIT"] =
        # diction["PID_TPSD"] =
        # diction["PID_DFHSIZE"] =
        # diction["PID_TIME"] =
        # diction["INTER"] =
        # diction["PID_VALID"] =
        # diction["PID_CHECK"] =
        # diction["PID_EVENT"] =
        # diction["PID_EVID"] =
        return diction

    def pic_dictionary(self):
        """Define elements for entry in pic table."""
        diction = {}
        diction["PIC_TYPE"] = self.pid["PID_TYPE"]
        diction["PIC_STYPE"] = self.pid["PID_STYPE"]
        # diction["PIC_PI1_OFF"] =
        # diction["PIC_PI1_WID"] =
        # diction["PIC_PI2_OFF"] =
        # diction["PIC_Pi2_WID"] =
        diction["PID_APID"] = self.pid["PID_APID"]
        return diction

    def tpcf_dictionary(self):
        """Define elements for entry in tpcf table."""
        diction = {}
        diction["TPCF_SPID"] = self.pid["PID_SPID"]
        try:
            diction["TPCF_NAME"] = self.structure.comment[-1].entries["text_id"]
        except:
            print(
                "Warn.:\tNot enough information specified for the packet: "
                + self.structure.entries[".type"]
                + "."
            )
        # diction["TPCF_SIZE"] =
        return diction

    def pcf_listdict(self):
        """Define elements for entries in pcf table."""
        entrydict = []
        for i in range(len(self.entries)):
            diction = {}
            size = self.positions[i + 1] - self.positions[i]
            try:
                no = "{:X}".format(
                    int(str(self.h_structure.comment[-1].entries["base_par_index"]), 16)
                    + i
                )
                diction["PCF_NAME"] = self.h_structure.comment[-1].entries[
                    "prefix"
                ] + str(no)
            except:
                diction["PCF_NAME"] = ""
                diction["PCF_DESCR"] = ""
            try:
                diction["PCF_DESCR"] = self.entries[i].comment[-1].entries["desc"]
            except:
                diction["PCF_DESCR"] = ""
            # diction["PCF_PID"] =
            try:
                diction["PCF_UNIT"] = self.entries[i].comment[-1].entries["unit"]
            except:
                diction["PCF_UNIT"] = ""
            diction["PCF_PTC"], diction["PCF_PCF"] = getptcpcf(self.entries[i], size)
            diction["PCF_WIDTH"] = size
            # diction["PCF_VALID"] =
            # diction["PCF_RELATED"] =
            diction["PCF_CATEG"] = categfromptc(diction["PCF_PTC"])
            # diction["PCF_NATUR"] =
            try:
                diction["PCF_CURTX"] = self.entries[i].comment[-1].entries["cal"]
            except:
                diction["PCF_CURTX"] = ""
            # diction["PCF_INTER"] =
            # diction["PCF_USCON"] =
            # diction["PCF_DECIM"] =
            # diction["PCF_PARVAL"] =
            # diction["PCF_SUBSYS"] =
            # diction["PCF_VALPAR"] =
            # diction["PCF_SPTYPE"] =
            # diction["PCF_CORR"] =
            # diction["PCF_OBTID"] =
            # diction["PCF_DARC"] =
            # diction["PCF_ENDIAN"] =
            # diction["PCF_DESCR2"] =
            entrydict.append(diction)
        return entrydict

    def plf_listdict(self):
        """Define elements for entries in plf table."""
        entrydict = []
        positions = [
            x + evalu("STRUCT_TMHEAD_SIZE") * 8 for x in self.positions
        ]  # this is ugly and should be replaced by some more rigorous approach later
        for i in range(len(self.entries)):
            diction = {}
            size = positions[i + 1] - positions[i]
            diction["PLF_NAME"] = self.pcf[i]["PCF_NAME"]
            diction["PLF_SPID"] = self.pid["PID_SPID"]
            diction["PLF_OFFBY"] = int(positions[i] / 8)
            diction["PLF_OFFBI"] = positions[i] - diction["PLF_OFFBY"] * 8
            # diction["PLF_NBOCC"] = abs(evalu(self.entries[i].array))
            # diction["PLF_LGOCC"] =
            # diction["PLF_TIME"] =
            # diction["PLF_TDOCC"] =
            entrydict.append(diction)
        return entrydict

    def cur_listdict(self):
        """Define elements for entries in cur table."""
        entrydict = []
        for l in range(len(self.entries)):
            i = self.entries[l]
            if len(i.comment) > 0 and "cal" in i.comment[-1].entries.keys():
                diction = {}
                diction["CUR_PNAME"] = self.pcf[l]["PCF_NAME"]
                diction["CUR_SELECT"] = i.comment[-1].entries["cal"]
                # diction["CUR_POS"] =
                # diction["CUR_RLCHK"] =
                # diction["CUR_VALPAR"] =
                entrydict.append(diction)
        return entrydict

    def header_search(self, typ):
        """Search for header information of the packet based on information in the comments."""
        hstruct = None
        for i in load.head1.structures:
            if i.type == "struct" and i.comment:
                uni = {}
                for l in i.comment:
                    uni.update(l.entries)
                if "pack_type" in uni.keys() and uni["pack_type"] == typ:
                    hstruct = i
        if hstruct == None and typ in load.enumerations.keys():
            hstruct = load.enumerations[typ]
        elif hstruct == None:
            print("Warn.:\t Wasn't able to establish the link of packet "+typ+" to any header structure.")
        return hstruct

    def h_analysis(self, h_struct):
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
                            for l in load.head1.structures + load.head2.structures:
                                if l.name == name:
                                    entries = entries + self.h_analysis(l)
                        else:
                            entries = entries + self.h_analysis(i.form)
        return entries

    def count_size(self):
        """Counts bit size of the packet header and bit position of entries within it."""
        size_bites = 0
        positions = []
        sizes = longdata.sizes
        for i in self.entries:
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
