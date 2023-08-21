"""This module holds methods used for formatting parsed data into commanding packet characteristics."""
import parsing.load as load
from construction.TM_packet_methods import count_size, evalu
from copy import copy

def packet_search(file):
    """Extract individual TC-packages from TC-header file."""
    packets = []
    for i in file.structures:
        if i.type == "struct" and i.comment and "packet" in i.comment[-1].entries.keys():
            packets.append(i)
    return packets
    
    
def h_analysis(h_struct):
    """Make a list of all individual (all structs unpacked) entries in the header of the packet."""
    entries_head = []
    entries = []
    if not (type(h_struct) is int or type(h_struct) is None):
        for i in h_struct.elements:
            if i.type not in {"enum", "struct"}:
                entries.append(i)
            elif i.type == "struct":
                occurences = 1
                from_struct = []
                if evalu(i.array) > 0:
                    occurences = evalu(i.array)
                for k in range(occurences):
                    if type(i.form) is str:
                        name = i.form
                        for l in load.TcH.structures + load.TcTmH.structures:
                            if l.name == name:
                                from_struct = [copy(x) for x in h_analysis(l)[1]]
                    else:
                        from_struct = [copy(x) for x in h_analysis(i.form)[1]]
                if i.name not in {"SpwHead","TcHead"}:
                    entries = entries + from_struct
                else:
                    entries_head = entries_head + from_struct
    return entries_head, entries

    
