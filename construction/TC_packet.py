"""This module takes care of creating a representation of commanding packets from parsed C-files and extracting entries for MIB databases."""
import parsing.load as load
import construction.TC_packet_methods as pm

class TC_header:
    """class representing the TC header common to all TC-packages"""

    def __init__(self, file):
        self.structure = self.find_header(file)

    def find_header(self, file):
        for i in file.structures:
            if "name" in i.__dir__() and i.name == "TcHead":
                return i
        print("Warn.:\tWasn't able to find the common Tc header.")


class TC_packet:
    """class representing each TC packet type and its properties"""

    def __init__(self, h_structure, header):
        self.h_structure = h_structure
        self.header = header
        self.h_entries, self.entries = pm.h_analysis(self.h_structure)
        self.size, self.positions = pm.count_size(self.entries)
        self.h_size, self.h_position = pm.count_size(self.h_entries)
        self.tcp = self.tcp_dictionary()
        self.pcpc = self.pcpc_listdict()
        
    def tcp_dictionary(self):
        """Define elements for entries in tcp table."""
        diction = {}
        try:
            diction["TCP_ID"] = self.h_structure.comment[-1].entries["text_id"]
        except:
            diction["TCP_ID"] = ""
        try:
            diction["TCP_DESC"] = self.h_structure.comment[-1].entries["desc"]
        except:
            diction["TCP_DESC"] = ""
        return diction
        
    def pcpc_listdict(self):
        """Define elements for entries in pcpc table."""
        entrydict = []
        for i in range(len(self.entries)):
            diction = {}
            try:
                no = "{:X}".format(
                    int(str(self.h_structure.comment[-1].entries["base_par_index"]), 16)
                    + i
                )
                diction["PCPC_PNAME"] = self.h_structure.comment[-1].entries[
                    "prefix"
                ] + str(no)
            except:
                diction["PCPC_PNAME"] = ""
            try:
                diction["PCPC_DESC"] = self.entries[i].comment[-1].entries["desc"]
            except:
                diction["PCPC_DESC"] = ""
            if self.entries[i].type[:4] in {"unit","unsi"}:
                diction["PCPC_CODE"] = "U"
            else:
                diction["PCPC_CODE"] = "I"
            entrydict.append(diction)
        return entrydict
