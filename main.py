"""This module works as a startpoint and intersection for the creation of the MIB databases."""
import load, gener, calib, packet


def main():
    """Run this whole hellish thing."""
    mcfs, txfs, cafs, lgfs = calib.calib_extract(load.head1.comments)
    gener.mcf_generate(mcfs)
    gener.txf_generate(txfs)
    gener.txp_generate(txfs)
    gener.caf_generate(cafs)
    gener.cap_generate(cafs)
    gener.lgf_generate(lgfs)
    lis = []
    for i in load.c_file.structures[1].elements:
        lis.append(packet.TM_packet(i))
    gener.pid_generate(lis)
    gener.pic_generate(lis)
    gener.tpcf_generate(lis)
    gener.pcf_generate(lis)
    gener.plf_generate(lis)
    return lis
