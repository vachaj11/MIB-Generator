"""Central location from which other modules can source data from files."""
import parh, parc

c1_path = "/home/vachaj11/Documents/MIB/start/src/PUS_TmDefs.c"
h1_path = "/home/vachaj11/Documents/MIB/start/src/PUS_TmDefs.h"
h2_path = "/home/vachaj11/Documents/MIB/start/src/PUS_TcTmDefs.h"
try:
    head1 = parh.main(h1_path)
    head2 = parh.main(h2_path)
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


enum1 = extr_values(head1)
enum2 = extr_values(head2)
enumerations = enum1 | enum2
