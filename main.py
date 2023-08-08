"""This module works as a startpoint and intersection for the creation of the MIB databases."""
import load, gener, calib, packet


def main():
    """Run this whole hellish thing."""
    cal = calib.calib_extract(load.head1.comments)
    gener.mcf_generate(cal["mcfs"])
    gener.txf_generate(cal["txfs"])
    gener.txp_generate(cal["txfs"])
    gener.caf_generate(cal["cafs"])
    gener.cap_generate(cal["cafs"])
    gener.lgf_generate(cal["lgfs"])
    lis = []
    for i in load.c_file.structures[1].elements:
        pack = packet.TM_packet(i)
        calib.cur_update(pack,cal)
        lis.append(pack)
    gener.pid_generate(lis)
    gener.pic_generate(lis)
    gener.tpcf_generate(lis)
    gener.pcf_generate(lis)
    gener.plf_generate(lis)
    gener.cur_generate(lis)
    return lis
