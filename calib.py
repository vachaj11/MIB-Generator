"""This module puts together all classes and function that represent the calibration part of MIB databases."""


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
                diction["MCF_POL" + str(i + 1)] = self.comment.entries["mcf"][
                    "a" + str(i)
                ]
            except:
                diction["MCF_POL" + str(i + 1)] = ""
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
                diction["LGF_POL" + str(i + 1)] = self.comment.entries["lgf"][
                    "a" + str(i)
                ]
            except:
                diction["LGF_POL" + str(i + 1)] = ""
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
