import parh, parc, longdata, gener

c1_path = "/home/vachaj11/Documents/MIB/start/src/PUS_TmDefs.c"
h1_path = "/home/vachaj11/Documents/MIB/start/src/PUS_TmDefs.h"
h2_path = "/home/vachaj11/Documents/MIB/start/src/PUS_TcTmDefs.h"
try:
    header1 = parh.main(h1_path)
    header2 = parh.main(h2_path)
    c_file = parc.main(c1_path)
except:
    print("Failed to load one of the C files")


def extr_values(file):
    """Search for constants, enum correspondences and other global values in the headers."""
    lis = {}
    for x in file.structures:
        if x.type == "enum":
            lis.update(x.entries)
        if x.type == "define":
            name = x.name
            if "(" in x.expression:
                value_raw = x.expression[1:-1]
            else:
                value_raw = x.expression
            try:
                value = int(value_raw)
            except:
                value = None
            if value is not None:
                lis[name] = value
    return lis


enum1 = extr_values(header1)
enum2 = extr_values(header2)
enumerations = enum1 | enum2


def apidnum(num):
    """Find the value of apid from evaluation of references, etc.
    I'm not following the direct logic of C here, because there seems to be some missing link."""
    lis = next((x for x in c_file.structures if x.name == "apidNum"), None)
    link = {}
    for i in lis.elements:
        link[str(enumerations[i.position[1:-1]])] = int(i.value)
    return link[str(num)]


def evalu(string):
    """Try evaluating the given expression using all known substitutions, macros, etc."""
    try:
        x = int(string)
    except:
        if string in enumerations.keys():
            x = enumerations[string]
        else:
            x = -1
            print("Wasn't able to find the numerical value of " + string)
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

    def pid_dictionary(self):
        """Define elements for entry in pid table."""
        diction = {}
        diction["PID_TYPE"] = evalu(self.structure.entries[".serviceType"])
        diction["PID_STYPE"] = evalu(self.structure.entries[".serviceSubType"])
        diction["PID_APID"] = apidnum(enumerations[self.structure.entries[".apid"]])
        # diction["PID_PI1_VAL"] =
        # diction["PID_PI_VAL"] =
        try:  # tired bodge
            diction["PID_SPID"] = self.structure.comment[-1].entries["num_id"]
            diction["PID_DESCR"] = self.structure.comment[-1].entries["desc"]
        except:
            diction["PID_SPID"] = ""
            diction["PID_DESCR"] = ""
            print(
                "Not enough information specified for the packet: "
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
                "Not enough information specified for the packet: "
                + self.structure.entries[".type"]
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
                no = "{:X}".format(int(str(self.h_structure.comment[-1].entries["base_par_index"]),16) + i)
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
            # diction["PCF_CURTX"] =
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
        positions = [x+evalu("STRUCT_TMHEAD_SIZE")*8 for x in self.positions] # this is ugly and should be replaced by some more rigorous approach later
        for i in range(len(self.entries)):
            diction = {}
            size = positions[i+1] - positions[i]
            diction["PLF_NAME"] = self.pcf[i]["PCF_NAME"]
            diction["PLF_SPID"] = self.pid["PID_SPID"]
            diction["PLF_OFFBY"] = int(positions[i]/8)
            diction["PLF_OFFBI"] = positions[i]-diction["PLF_OFFBY"]*8
            #diction["PLF_NBOCC"] = abs(evalu(self.entries[i].array))
            #diction["PLF_LGOCC"] =
            #diction["PLF_TIME"] =
            #diction["PLF_TDOCC"] =
            entrydict.append(diction)
        return entrydict

    def header_search(self, typ):
        """Search for header information of the packet based on information in the comments.""" 
        hstruct = None
        for i in header1.structures:
            if i.type == "struct" and i.comment:
                uni = {}
                for l in i.comment:
                    uni.update(l.entries)
                if "pack_type" in uni.keys() and uni["pack_type"] == typ:
                    hstruct = i
        if hstruct == None and typ in enumerations.keys():
            hstruct = enumerations[typ]
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
                            for l in header1.structures + header2.structures:
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
        
        
def calib_extract(comments):
    """Extract declaration of various calibrations if they occur in the comments"""
    mcfs = []
    txfs = []
    cafs = []
    lgfs = []
    for i in comments:
        keys = i.entries.keys()
        if "cal_def" in keys:
            if "mcf" in keys:
                mcfs.append(mcf_calib(i))
            elif "text_cal" in keys:
                txfs.append(txf_calib(i))
            elif "lgf" in keys:
                lgfs.append(lgf_calib(i))
            elif "num_cal" in keys:
                cafs.append(caf_calib(i))
    return mcfs, txfs, cafs, lgfs


class mcf_calib:
    """class of a mcf calibration"""
    def __init__(self, comment):
        self.comment = comment
        self.mcf = self.mcf_dictionary()
        
    def mcf_dictionary(self):
        """Define elements for entry in mcf table."""
        diction = {}
        diction["MCF_IDENT"] = self.comment.entries["cal_ident"]
        diction["MCF_DESCR"] = self.comment.entries["desc"]
        for i in range(5):
            try:
                diction["MCF_POL"+str(i+1)] = self.comment.entries["mcf"]["a"+str(i)]
            except:
                diction["MCF_POL"+str(i+1)] = ""
        return diction
        
        
class lgf_calib:
    """class of a lgf calibration"""
    def __init__(self, comment):
        self.comment = comment
        self.lgf = self.lgf_dictionary()
        
    def lgf_dictionary(self):
        """Define elements for entry in lgf table."""
        diction = {}
        diction["LGF_IDENT"] = self.comment.entries["cal_ident"]
        diction["LGF_DESCR"] = self.comment.entries["desc"]
        for i in range(5):
            try:
                diction["LGF_POL"+str(i+1)] = self.comment.entries["lgf"]["a"+str(i)]
            except:
                diction["LGF_POL"+str(i+1)] = ""
        return diction


class txf_calib:
    """class of a txf calibration"""
    def __init__(self, comment):
        self.comment = comment
        self.type, self.length = self.txf_data()
        self.txf = self.txf_dictionary()
        self.txp = self.txp_listdict()
        
    def txf_data(self):
        """Get information about the nature of data calibrated."""
        try:
            minim = self.comment.entries["text_cal"]["min"]
            if type(minim) is not int:
                flav = "R"
            elif minim < 0:
                flav = "I"
            else:
                flav = "U"
            leng = str(len(self.comment.entries["text_cal"]["lookup"]))
        except:
            flav = ""
            leng = ""
        return flav, leng
        
    def txf_dictionary(self):
        """Define elements for entry in txf table."""
        diction = {}
        diction["TXF_NUMBR"] = self.comment.entries["cal_ident"]
        diction["TXF_DESCR"] = self.comment.entries["desc"]
        diction["TXF_RAWFMT"] = self.type
        diction["TXF_NALIAS"] = self.length
        return diction
        
    def txp_listdict(self):
        """Define elements for entry in txp table."""
        entrydict = []
        for i in self.comment.entries["text_cal"]["lookup"]:
            diction = {}
            diction["TXP_NUMBR"] = self.txf["TXF_NUMBR"]
            try:
                if "val" in i.keys():
                    diction["TXP_FROM"] = i["val"]
                    diction["TXP_TO"] = i["val"]
                else:
                    diction["TXP_FROM"] = i["from"]
                    diction["TXP_TO"] = i["to"]
                diction["TXP_ALTXT"] = i["text"]
            except:
                diction["TXP_FROM"] = ""
                diction["TXP_TO"] = ""
                diction["TXP_ALTXT"] = ""
            entrydict.append(diction)
        return entrydict
        
class caf_calib:
    """class of a caf calibration"""
    def __init__(self, comment):
        self.comment = comment
        self.type, self.length = self.caf_data()
        self.caf = self.caf_dictionary()
        self.cap = self.cap_listdict()
        
    def caf_data(self):
        """Get information about the nature of data calibrated."""
        try:
            entries = self.comment.entries["num_cal"]
            raw = []
            eng = []
            for i in entries:
                raw.append(i[0])
                eng.append(i[1])
            if type(sum(raw)) is not int:
                flav_r = "R"
            elif min(raw) < 0:
                flav_r = "I"
            else:
                flav_r = "U"
            if type(sum(eng)) is not int:
                flav_e = "R"
            elif min(eng) < 0:
                flav_e = "I"
            else:
                flav_e = "U"
            leng = str(len(self.comment.entries["num_cal"]))
        except:
            flav_r = ""
            flav_e = ""
            leng = ""
        return [flav_r,flav_e], leng
        
    def caf_dictionary(self):
        """Define elements for entry in caf table."""
        diction = {}
        diction["CAF_NUMBR"] = self.comment.entries["cal_ident"]
        diction["CAF_DESCR"] = self.comment.entries["desc"]
        diction["CAF_ENGFMT"] = self.type[1]
        diction["CAF_RAWFMT"] = self.type[0]
        #diction["CAF_RADIX"] =
        #diction["CAF_UNIT"] =
        diction["CAF_NCURVE"] = self.length
        #diction["CAF_INTER"] =
        return diction
        
    def cap_listdict(self):
        """Define elements for entry in cap table."""
        entrydict = []
        for i in self.comment.entries["num_cal"]:
            diction = {}
            diction["CAP_NUMBR"] = self.caf["CAF_NUMBR"]
            diction["CAP_XVALS"] = i[0]
            diction["CAP_YVALS"] = i[1]
            entrydict.append(diction)
        return entrydict


def main():
    """Run this whole hellish thing."""
    mcfs, txfs, cafs, lgfs = calib_extract(header1.comments)
    gener.mcf_generate(mcfs)
    gener.txf_generate(txfs)
    gener.txp_generate(txfs)
    gener.caf_generate(cafs)
    gener.cap_generate(cafs)
    gener.lgf_generate(lgfs)
    lis = []
    for i in c_file.structures[1].elements:
        lis.append(TM_packet(i))
    gener.pid_generate(lis)
    gener.pic_generate(lis)
    gener.tpcf_generate(lis)
    gener.pcf_generate(lis)
    gener.plf_generate(lis)
    return lis
