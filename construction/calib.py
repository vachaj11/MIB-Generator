"""This module puts together all classes and function that represent the calibration and verification parts of MIB databases."""
import parsing.load as load


def cur_update(packet, cal):
    """Check whether calibration exists for parameters which require it and if yes, change cur entries correspondingly"""
    calibs = []
    for i in cal:
        for l in cal[i]:
            calibs.append(l)
    for i in packet.cur:
        match_count = 0
        for l in calibs:
            if i["CUR_SELECT"] == l.name:
                i["CUR_SELECT"] = l.comment.entries["cal_ident"]
                match_count += 1
        if match_count == 0:
            print(
                "Warn.:\tWasn't able to find matching calibration for "
                + i["CUR_PNAME"]
                + " in packet "
                + str(packet.pid["PID_SPID"])
            )
            packet.cur.remove(i)
    for i in packet.pcf:
        if "PCF_CURTX" in i.keys() and i["PCF_CURTX"]:
            match_count = 0
            for l in calibs:
                if i["PCF_CURTX"] == l.name:
                    i["PCF_CURTX"] = l.comment.entries["cal_ident"]
                    match_count += 1
                    if "txf" in l.__dir__():
                        i["PCF_CATEG"] = "S"
            if match_count == 0:
                print(
                    "Warn.:\tWasn't able to find matching calibration for "
                    + i["PCF_CURTX"]
                    + " in packet "
                    + str(packet.pid["PID_SPID"])
                )
                i["PCF_CURTX"] = ""


def cpc_update(command, dec):
    """Check whether decalibration exists for parameter which require it and if yes, change cpc entry correspondingly."""
    for i in command.cpc:
        if "CPC_PAFREF" in i.keys() and i["CPC_PAFREF"]:
            match_count = 0
            for l in dec:
                if i["CPC_PAFREF"] == l.name:
                    i["CPC_PAFREF"] = l.comment.entries["dec_ident"]
                    match_count += 1
            if match_count == 0:
                print(
                    "Warn.:\tWasn't able to find matching decalibration for "
                    + i["CPC_PAFREF"]
                    + " in command "
                    + str(command.ccf["CCF_CNAME"])
                )
                i["CPC_PAFREF"] = ""


def calib_extract(comments):
    """Extract declaration of various calibrations if they occur in the comments"""
    mcfs = []
    txfs = []
    cafs = []
    lgfs = []
    for i in comments:
        keys = i.entries.keys()
        if "cal_ident" in keys:
            if "mcf" in keys:
                mcfs.append(mcf_calib(i))
            elif bool({"text_cal", "enum"} & keys):
                txfs.append(txf_calib(i))
            elif "lgf" in keys:
                lgfs.append(lgf_calib(i))
            elif "num_cal" in keys:
                cafs.append(caf_calib(i))
    return {"mcfs": mcfs, "txfs": txfs, "cafs": cafs, "lgfs": lgfs}


def decal_extract(comments):
    """Extract declarations of decalibrations from comments."""
    decal = []
    for i in comments:
        if "dec_ident" in i.entries.keys():
            decal.append(decalib(i))
    return decal


class calib:
    """general class of calibration"""

    def __init__(self, comment):
        self.comment = comment
        if "cal_def" in comment.entries.keys():
            self.name = comment.entries["cal_def"]
        else:
            self.name = comment.entries["enum"]


class mcf_calib(calib):
    """class of a mcf calibration"""

    def __init__(self, comment):
        calib.__init__(self, comment)
        self.mcf = self.mcf_dictionary()

    def mcf_dictionary(self):
        """Define elements for entry in mcf table."""
        diction = {}
        diction["MCF_IDENT"] = self.comment.entries["cal_ident"]
        diction["MCF_DESCR"] = self.comment.entries["desc"]
        for i in range(5):
            try:
                diction["MCF_POL" + str(i + 1)] = self.comment.entries["mcf"][
                    "a" + str(i)
                ]
            except:
                diction["MCF_POL" + str(i + 1)] = ""
        return diction


class lgf_calib(calib):
    """class of a lgf calibration"""

    def __init__(self, comment):
        calib.__init__(self, comment)
        self.lgf = self.lgf_dictionary()

    def lgf_dictionary(self):
        """Define elements for entry in lgf table."""
        diction = {}
        diction["LGF_IDENT"] = self.comment.entries["cal_ident"]
        diction["LGF_DESCR"] = self.comment.entries["desc"]
        for i in range(5):
            try:
                diction["LGF_POL" + str(i + 1)] = self.comment.entries["lgf"][
                    "a" + str(i)
                ]
            except:
                diction["LGF_POL" + str(i + 1)] = ""
        return diction


class txf_calib(calib):
    """class of a txf calibration"""

    def __init__(self, comment):
        calib.__init__(self, comment)
        self.enum = self.is_enum()
        self.type, self.length = self.txf_data()
        self.txf = self.txf_dictionary()
        self.txp = self.txp_listdict()

    def is_enum(self):
        """Check whether the calibration is saved in the header file as enum."""
        if "enum" in self.comment.entries.keys():
            return True
        else:
            return False

    def txf_data(self):
        """Get information about the nature of data calibrated."""
        try:
            if not self.enum:
                minim = self.comment.entries["text_cal"]["min"]
                leng = str(len(self.comment.entries["text_cal"]["lookup"]))
            else:
                minim = min(self.comment.structure.entries.values())
                leng = len(self.comment.structure.entries)
            if type(minim) is not int:
                flav = "R"
            elif minim < 0:
                flav = "I"
            else:
                flav = "U"
        except:
            flav = ""
            leng = ""
        return flav, leng

    def txf_dictionary(self):
        """Define elements for entry in txf table."""
        diction = {}
        diction["TXF_NUMBR"] = self.comment.entries["cal_ident"]
        try:
            diction["TXF_DESCR"] = self.comment.entries["desc"]
        except:
            diction["TXF_DESCR"] = ""
        diction["TXF_RAWFMT"] = self.type
        diction["TXF_NALIAS"] = self.length
        return diction

    def txp_listdict(self):
        """Define elements for entry in txp table."""
        entrydict = []
        if not self.enum:
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
        else:
            entries = list(self.comment.structure.entries.items())
            for i in range(len(entries)):
                diction = {}
                diction["TXP_NUMBR"] = self.txf["TXF_NUMBR"]
                diction["TXP_FROM"] = entries[i][1]
                diction["TXP_TO"] = entries[i][1]
                try:
                    diction["TXP_ALTXT"] = self.comment.structure.comment[
                        -self.length + i
                    ].entries["text"]
                except:
                    diction["TXP_ALTXT"] = "-1"
                entrydict.append(diction)
        return entrydict


class caf_calib(calib):
    """class of a caf calibration"""

    def __init__(self, comment):
        calib.__init__(self, comment)
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
        return [flav_r, flav_e], leng

    def caf_dictionary(self):
        """Define elements for entry in caf table."""
        diction = {}
        diction["CAF_NUMBR"] = self.comment.entries["cal_ident"]
        diction["CAF_DESCR"] = self.comment.entries["desc"]
        diction["CAF_ENGFMT"] = self.type[1]
        diction["CAF_RAWFMT"] = self.type[0]
        # diction["CAF_RADIX"] =
        # diction["CAF_UNIT"] =
        diction["CAF_NCURVE"] = self.length
        # diction["CAF_INTER"] =
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


class decalib(calib):
    """class of a text decalibration"""

    def __init__(self, comment):
        calib.__init__(self, comment)
        self.type, self.length = self.paf_data()
        self.paf = self.paf_dictionary()
        self.pas = self.pas_listdict()

    def paf_data(self):
        """Get information about the nature of data calibrated."""
        try:
            minim = min(self.comment.structure.entries.values())
            leng = len(self.comment.structure.entries)
            if type(minim) is not int:
                flav = "R"
            elif minim < 0:
                flav = "I"
            else:
                flav = "U"
        except:
            flav = ""
            leng = ""
        return flav, leng

    def paf_dictionary(self):
        """Define elements for entry in paf table."""
        diction = {}
        diction["PAF_NUMBR"] = self.comment.entries["dec_ident"]
        try:
            diction["PAF_DESCR"] = self.comment.entries["desc"]
        except:
            diction["PAF_DESCR"] = ""
        diction["PAF_RAWFMT"] = self.type
        diction["PAF_NALIAS"] = self.length
        return diction

    def pas_listdict(self):
        """Define elements for entry in pas table."""
        entrydict = []
        entries = list(self.comment.structure.entries.items())
        for i in range(len(entries)):
            diction = {}
            diction["PAS_NUMBR"] = self.paf["PAF_NUMBR"]
            diction["PAS_ALVAL"] = entries[i][1]
            try:
                diction["PAS_ALTXT"] = self.comment.structure.comment[
                    -self.length + i
                ].entries["text"]
            except:
                diction["PAS_ALTXT"] = "-1"
            entrydict.append(diction)
        return entrydict
        
        
def verif_extract(comments):
    """Extract declarations of verifications from comments."""
    verif = []
    for i in comments:
        if "cvs_def" in i.entries.keys():
            verif.append(verification(i))
    return verif
    

def cvs_update(command, verifs):
    if command.cvp is None:
        entrydict = []
        for i in verifs:
            diction = {}
            diction["CVP_TASK"] = command.ccf["CCF_CNAME"]
            diction["CVP_TYPE"] = "C"
            diction["CVP_CVSID"] = i.cvs["CVS_ID"]
            entrydict.append(diction)
        command.cvp =  entrydict
    else:
        lis = []
        for i in verifs:
            lis.append(i.cvs["CVS_ID"])
        maxi = len(command.cvp)
        for i in range(maxi):
            if command.cvp[maxi-1-i]["CVP_CVSID"] not in lis:
                print(
                    "Warn.:\tWasn't able to find the required verification "
                    + str(command.cvp[maxi-1-i]["CVP_CVSID"])
                    + " for command "
                    + str(command.ccf["CCF_CNAME"])
                )
                command.cvp.pop(maxi-i-1)
            

class verification:
    """class of command verification"""
    def __init__(self,comment):
        self.comment = comment
        self.cvs = self.cvs_dictionary()
        
    def cvs_dictionary(self):
        """Define elements for entry in cvs table."""
        diction = {}
        diction["CVS_ID"] = self.comment.entries["cvs_def"]
        try:
            diction["CVS_TYPE"] = self.comment.entries["cvs_type"]
        except:
            diction["CVS_TYPE"] = ""
        if "cve" in self.comment.entries.keys():
            diction["CVS_SOURCE"] = "V"
        else:
            diction["CVS_SOURCE"] = "R"
        try:
            diction["CVS_START"] = self.comment.entries["cvs_start"]
        except:
            diction["CVS_START"] = 0
        try:
            diction["CVS_INTERVAL"] = self.comment.entries["cvs_interval"]
        except:
            diction["CVS_INTERVAL"] = ""
        # diction["CVS_SPID"] = ""
        # diction["CVS_UNCERTAINTY"] = ""
        return diction
