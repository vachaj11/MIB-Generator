"""This module works as a startpoint and intersection for the creation of the MIB databases."""
import load, gener, calib, packet
import argparse


def main(visual = True, generate = True):
    """Run this whole hellish thing."""
    cal = calib.calib_extract(load.head1.comments)
    lis = []
    for i in load.c_file.structures[1].elements:
        pack = packet.TM_packet(i)
        calib.cur_update(pack, cal)
        lis.append(pack)
    if generate:
        gener.mcf_generate(cal["mcfs"])
        gener.txf_generate(cal["txfs"])
        gener.txp_generate(cal["txfs"])
        gener.caf_generate(cal["cafs"])
        gener.cap_generate(cal["cafs"])
        gener.lgf_generate(cal["lgfs"])
        gener.pid_generate(lis)
        gener.pic_generate(lis)
        gener.tpcf_generate(lis)
        gener.pcf_generate(lis)
        gener.plf_generate(lis)
        gener.cur_generate(lis)
    if visual:
        try:
            import visualiser

            visualiser.main([load.head1, load.head2, load.c_file])
        except ModuleNotFoundError:
            print("Please install PySide6 in order to show the parsed files.")
    return lis


if __name__ == "__main__":
    prog = "MIB Creator"
    desc = "Creates MIB databases from C-files defined in paths.json5"
    parser = argparse.ArgumentParser(prog = prog, description = desc)
    parser.add_argument("-v","--visualise",help="show the contents of parsed files in GUI", action = "store_true")
    parser.add_argument("-g","--xgenerate", help="run without generating MIB files", action = "store_true")
    arguments = parser.parse_args()
    main(arguments.visualise, not arguments.xgenerate)
