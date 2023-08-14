"""This module takes care of creating a representation of packets from parsed C-files and extracting entries for MIB databases."""
import packet_methods as pm
class TM_header:
    """class representing the TM header common to all TM-packages"""
    def __init__(self, file):
        self.structure = self.find_header(file)
        self.entries = pm.h_analysis(self.structure)
        self.size, self.positions = pm.count_size(self.entries)
        
    def find_header(self, file):
        for i in file.structures:
            methods = i.__dir__()
            if "name" in methods and i.name == "TmHead":
                return i
        print("Warn.:\tWasn't able to find the common Tm header.")
        

class TM_packet:
    """class representing each TM packet type and its properties"""

    def __init__(self, structure, header):
        self.structure = structure
        self.header = header
        self.h_structure = pm.header_search(structure.entries[".type"])
        self.entries = pm.h_analysis(self.h_structure)
        self.var_entries = pm.var_get(self.entries)
        self.size, self.positions = pm.count_size(self.entries)
        self.pid = self.pid_dictionary()
        self.pic = self.pic_dictionary()
        self.tpcf = self.tpcf_dictionary()
        self.pcf = self.pcf_listdict()
        self.plf = self.plf_listdict()
        self.cur = self.cur_listdict()

    def pid_dictionary(self):
        """Define elements for entry in pid table."""
        diction = {}
        diction["PID_TYPE"] = pm.evalu(self.structure.entries[".serviceType"])
        diction["PID_STYPE"] = pm.evalu(self.structure.entries[".serviceSubType"])
        diction["PID_APID"] = pm.apidnum(self.structure.entries[".apid"])
        # diction["PID_PI1_VAL"] =
        # diction["PID_PI_VAL"] =
        try:
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
        if self.var_entries:
            diction["PID_TPSD"] = diction["PID_SPID"]
        else:
            diction["PID_TPSC"] = "-1"
        diction["PID_DFHSIZE"] = self.header.size
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
        comm = self.structure.comment
        diction["PIC_TYPE"] = self.pid["PID_TYPE"]
        diction["PIC_STYPE"] = self.pid["PID_STYPE"]
        if comm and "add_id1" in comm[-1].entries.keys():
            diction["PIC_PI1_OFF"] = self.header.size
            # + something probably, this would have to be further specified somewhere
            diction["PIC_PI1_WID"] = ""
            diction["PIC_PI2_OFF"] = self.header.size
            diction["PIC_PI2_WID"] = ""
        else:
            diction["PIC_PI1_OFF"] = -1
            diction["PIC_PI1_WID"] = 0
            diction["PIC_PI2_OFF"] = -1
            diction["PIC_PI2_WID"] = 0
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
            diction["PCF_PTC"], diction["PCF_PFC"] = pm.getptcpcf(self.entries[i], size)
            diction["PCF_WIDTH"] = size
            # diction["PCF_VALID"] =
            # diction["PCF_RELATED"] =
            diction["PCF_CATEG"] = pm.categfromptc(diction["PCF_PTC"])
            # this uses probably a wrong specification of natur
            try:
                diction["PCF_NATUR"] = self.entries[i].comment[-1].entries["nature"]
            except:
                diction["PCF_NATUR"] = "R"
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
            x + self.header.size * 8 for x in self.positions
        ]
        for i in range(len(self.entries)):
            diction = {}
            size = positions[i + 1] - positions[i]
            diction["PLF_NAME"] = self.pcf[i]["PCF_NAME"]
            diction["PLF_SPID"] = self.pid["PID_SPID"]
            diction["PLF_OFFBY"] = int(positions[i] / 8)
            diction["PLF_OFFBI"] = positions[i] - diction["PLF_OFFBY"] * 8
            # diction["PLF_NBOCC"] = abs(pm.evalu(self.entries[i].array))
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
            # this will have to be modified when I get how multiple calibrations will look in comments
            if i.comment and "cals" in i.comment[-1].entries.keys():
                diction = {}
                diction["CUR_PNAME"] = self.pcf[l]["PCF_NAME"]
                diction["CUR_SELECT"] = i.comment[-1].entries["cal"]
                # diction["CUR_POS"] =
                # diction["CUR_RLCHK"] =
                # diction["CUR_VALPAR"] =
                entrydict.append(diction)
        return entrydict
