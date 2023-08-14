"""Central location from which other modules can source data from the parsed C-files."""
import parh, parc, json5

file = open("paths.json5", "r")
paths = json5.load(file)
file.close()

c1_path = paths["TmFile"]
h1_path = paths["TmHeader"]
h2_path = paths["TcTmHeader"]
out_dir = paths["OutDir"]

try:
    head1 = parh.main(h1_path)
    head2 = parh.main(h2_path)
    c_file = parc.main(c1_path)
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


enum1 = extr_values(head1)
enum2 = extr_values(head2)
enumerations = enum1 | enum2
