"""This module works as a startpoint and intersection for the creation of the MIB databases."""
import load, gener, calib, packet
import argparse
import packet_methods


def main(visual=True, generate=True, parseonly=False):
    """Run this whole hellish thing."""
    lis = []
    if not parseonly:
        cal = calib.calib_extract(load.TmH.comments)
        TmHead = packet.TM_header(load.TmH)
        for i in load.TmC.structures[1].elements:
            matched = packet_methods.header_search(i.entries[".type"])
            for k in matched:
                pack = packet.TM_packet(i, k, TmHead)
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

            visualiser.main([load.TmH, load.TcTmH, load.TmC])
        except ModuleNotFoundError:
            print(
                "Warn.:\tPySide6 not found. Please install it in order to show the parsed files."
            )
    return lis


if __name__ == "__main__":
    prog = "MIB Creator"
    desc = "Creates MIB databases from C-files defined in paths.json5"
    parser = argparse.ArgumentParser(prog=prog, description=desc)
    parser.add_argument(
        "-v",
        "--visualise",
        help="show the contents of parsed files in GUI (requires PySide6 installed)",
        action="store_true",
    )
    parser.add_argument(
        "-x",
        "--xgenerate",
        help="run without generating MIB files",
        action="store_true",
    )
    parser.add_argument(
        "-o",
        "--onlyparse",
        help="stop after parsing the C-files (does not also generate MIB files)",
        action="store_true",
    )
    arguments = parser.parse_args()
    main(arguments.visualise, not arguments.xgenerate, arguments.onlyparse)
