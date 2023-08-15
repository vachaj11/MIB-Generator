"""Central location from which other modules can source data from the parsed C-files."""
import json5

import parsing.parh as parh
import parsing.parc as parc

file = open("data/paths.json5", "r")
paths = json5.load(file)
file.close()

TmC_path = paths["TmFile"]
TmH_path = paths["TmHeader"]
TcTmH_path = paths["TcTmHeader"]
out_dir = paths["OutDir"]

try:
    TmH = parh.main(TmH_path)
    TcTmH = parh.main(TcTmH_path)
    TmC = parc.main(TmC_path)
except:
    print("Error:\tFailed to load one of the C files")
    exit()


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


enum1 = extr_values(TmH)
enum2 = extr_values(TcTmH)
enumerations = enum1 | enum2
