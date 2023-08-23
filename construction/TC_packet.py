"""This module takes care of creating a representation of commanding packets from parsed C-files and extracting entries for MIB databases."""
import parsing.load as load
import construction.TC_packet_methods as pm


class TC_header:
    """class representing the TC header common to all TC-packages"""

    def __init__(self, structure):
        self.structure = structure
        self.entries = pm.h_analysis(self.structure)[1]
        self.size, self.positions = pm.count_size(self.entries)
        self.parameters = pm.param_list(self.entries)
        self.tcp = self.tcp_dictionary()
        self.pcpc = self.pcpc_listdict()
        self.pcdf = self.pcdf_listdict()

    def tcp_dictionary(self):
        """Define elements for entries in tcp table."""
        diction = {}
        try:
            diction["TCP_ID"] = self.structure.comment[-1].entries["text_id"]
        except:
            diction["TCP_ID"] = self.structure.name
        try:
            diction["TCP_DESC"] = self.structure.comment[-1].entries["desc"]
        except:
            diction["TCP_DESC"] = ""
        return diction

    def pcpc_listdict(self):
        """Define elements for entries in pcpc table."""
        entrydict = []
        for i in range(len(self.entries)):
            if self.parameters[i] >= 0:
                diction = {}
                try:
                    no = "{:X}".format(
                        int(
                            str(self.structure.comment[-1].entries["base_par_index"]),
                            16,
                        )
                        + i
                    )
                    diction["PCPC_PNAME"] = self.structure.comment[-1].entries[
                        "prefix"
                    ] + str(no)
                except:
                    diction["PCPC_PNAME"] = self.entries[i].name
                try:
                    diction["PCPC_DESC"] = self.entries[i].comment[-1].entries["desc"]
                except:
                    diction["PCPC_DESC"] = ""
                if self.entries[i].type[:4] in {"unit", "unsi"}:
                    diction["PCPC_CODE"] = "U"
                else:
                    diction["PCPC_CODE"] = "I"
                entrydict.append(diction)
        return entrydict

    def pcdf_listdict(self):
        """Define elements for entries in pcpc table."""
        entrydict = []
        for i in range(len(self.entries)):
            diction = {}
            diction["PCDF_TCNAME"] = self.tcp["TCP_ID"]
            diction["PCDF_DESC"] = self.pcpc[self.parameters[i]]["PCPC_DESC"]
            match self.entries[i].name:
                case "apid":
                    diction["PCDF_TYPE"] = "A"
                case "serviceType":
                    diction["PCDF_TYPE"] = "T"
                case "subType":
                    diction["PCDF_TYPE"] = "S"
                case _:
                    if self.parameters[i] < 0:
                        diction["PCDF_TYPE"] = "F"
                    else:
                        diction["PCDF_TYPE"] = "P"
            diction["PCDF_LEN"] = int(self.positions[i + 1] - self.positions[i])
            diction["PCDF_BIT"] = self.positions[i]
            if diction["PCDF_TYPE"] != "F":
                diction["PCDF_PNAME"] = self.pcpc[self.parameters[i]]["PCPC_PNAME"]
            # There should definitely be some default values here.
            # diction["PCDF_VALUE"] = ""
            # diction["PCDF_RADIX"] = ""
            entrydict.append(diction)
        return entrydict


class TC_packet:
    """class representing each TC packet type and its properties"""

    def __init__(self, h_structure, header):
        self.h_structure = h_structure
        self.header = header
        self.h_entries, self.entries = pm.h_analysis(self.h_structure)
        self.size, self.positions = pm.count_size(self.entries)
        self.h_size, self.h_position = pm.count_size(self.h_entries)
        self.parameters = pm.param_list(self.entries)
        self.ccf = self.ccf_dictionary()
        self.cpc = self.cpc_listdict()
        self.cdf = self.cdf_listdict()

    def ccf_dictionary(self):
        """Define elements for entries in ccf table."""
        diction = {}
        try:
            diction["CCF_CNAME"] = self.h_structure.comment[-1].entries["text_id"]
        except:
            diction["CCF_CNAME"] = ""
        try:
            diction["CCF_DESCR"] = self.h_structure.name
        except:
            diction["CCF_DESCR"] = ""
        try:
            diction["CCF_DESCR2"] = self.h_structure.comment[-1].entries["desc"]
        except:
            diction["CCF_DESCR2"] = ""
        # diction["CCF_CTYPE"] = ""
        # diction["CCF_CRITICAL"] = ""
        diction["CCF_PKTID"] = self.header.tcp["TCP_ID"]
        try:
            diction["CCF_TYPE"] = self.h_structure.comment[-1].entries["service"]
            diction["CCF_STYPE"] = self.h_structure.comment[-1].entries["sub"]
        except:
            diction["CCF_TYPE"] = ""
            diction["CCF_STYPE"] = ""
        # diction["CCF_APID"] = ""
        diction["CCF_NPARS"] = len(self.entries)
        # diction["CCF_PLAN"] = ""
        # diction["CCF_EXEC"] = ""
        # diction["CCF_ILSCOPE"] = ""
        # diction["CCF_ILSTAGE"] = ""
        # diction["CCF_SUBSYS"] = ""
        # diction["CCF_HIPRI"] = ""
        # diction["CCF_MAPID"] = ""
        # diction["CCF_DEFSET"] = ""
        # diction["CCF_RAPID"] = ""
        # diction["CCF_ACK"] = ""
        # diction["CCF_SUBSCHEDID"] = ""
        return diction

    def cpc_listdict(self):
        """Define elements for entries in cpc table."""
        entrydict = []
        for i in range(len(self.entries)):
            if self.parameters[i] >= 0:
                diction = {}
                size = int(self.positions[i + 1] - self.positions[i])
                try:
                    no = "{:X}".format(
                        int(
                            str(self.h_structure.comment[-1].entries["base_par_index"]),
                            16,
                        )
                        + i
                    )
                    diction["CPC_PNAME"] = self.h_structure.comment[-1].entries[
                        "prefix"
                    ] + str(no)
                except:
                    diction["CPC_PNAME"] = ""
                try:
                    diction["CPC_DESCR"] = self.entries[i].comment[-1].entries["desc"]
                except:
                    diction["CPC_DESCR"] = ""
                diction["CPC_PTC"], diction["CPC_PFC"] = pm.getptcpcf(
                    self.entries[i], size
                )
                try:
                    if {"cal", "enum"} & self.entries[i].comment[-1].entries.keys():
                        diction["CPC_CATEG"] = "T"
                    else:
                        diction["CPC_CATEG"] = ""
                except:
                    diction["CPC_CATEG"] = ""
                if diction["CPC_CATEG"] == "T":
                    diction["CPC_DISPFMT"] = "A"
                elif diction["CPC_PTC"] == 9:
                    diction["CPC_DISPFMT"] = "T"
                elif diction["CPC_PTC"] == 10:
                    diction["CPC_DISPFMT"] = "D"
                else:
                    diction["CPC_DISPFMT"] = "U"
                # diction["CPC_RADIX"] = ""
                try:
                    diction["CPC_UNIT"] = self.entries[i].comment[-1].entries["unit"]
                except:
                    diction["CPC_UNIT"] = ""
                # diction["CPC_PRFREF"] = ""
                # diction["CPC_CCAREF"] = ""
                # diction["CPC_PAFREF"] = ""
                # diction["CPC_INTER"] = ""
                # diction["CPC_DEFVAL"] = ""
                # diction["CPC_CORR"] = ""
                # diction["CPC_OBTID"] = ""
                # diction["CPC_DESCR2"] = ""
                # diction["CPC_ENDIAN"] = ""
                entrydict.append(diction)
        return entrydict

    def cdf_listdict(self):
        """Define elements for entries in cdf table."""
        entrydict = []
        gr_size = pm.get_gr_sizes(self.entries)
        for i in range(len(self.entries)):
            size = int(self.positions[i + 1] - self.positions[i])
            diction = {}
            diction["CDF_CNAME"] = self.ccf["CCF_CNAME"]
            if self.parameters[i] < 0:
                diction["CDF_ELTYPE"] = "A"
            else:
                diction["CDF_ELTYPE"] = "E"
            try:
                diction["CDF_DESCR"] = self.entries[i].comment[-1].entries["desc"]
            except:
                diction["CDF_DESCR"] = ""
            diction["CDF_ELLEN"] = size
            diction["CDF_BIT"] = self.positions[i]
            diction["CDF_GRPSIZE"] = gr_size[i]
            if diction["CDF_ELTYPE"] in {"E", "F"}:
                diction["CDF_PNAME"] = self.cpc[self.parameters[i]]["CPC_PNAME"]
            else:
                diction["CDF_PNAME"] = ""
            # diction["CDF_INTER"] = ""
            if diction["CDF_ELTYPE"] != "A":
                try:
                    diction["CDF_VALUE"] = pm.evalu(
                        self.entries[i].comment[-1].entries["default"]
                    )
                except:
                    diction["CDF_VALUE"] = ""
            else:
                try:
                    diction["CDF_VALUE"] = pm.evalu(
                        self.entries[i].comment[-1].entries["default"]
                    )
                except:
                    diction["CDF_VALUE"] = 0
            # diction["CDF_TMID"] = ""
            entrydict.append(diction)
        return entrydict
