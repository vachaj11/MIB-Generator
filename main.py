"""This module works as a startpoint and a junction for creation of the MIB databases.

If ran directly as a Python script, this module provides the user with a simple CLI which allows for specification of
various options for runtime of the script itself (whether the MIB databases should be constructed, whether saved, 
whether the parsed file should be visualised, etc..). It also provides a quick ``--help`` summary and an option to
run scripts for updating the config and paths files before running the generating script itself. The main generating
script is then called through the :obj:`main` method.
"""
import argparse


def main(visual=False, generate=True, parseonly=False, paths=False, config=False):
    """Run this whole hellish thing.
    
    This method holds the main logic of the whole program. Roughly it sequentially does this:
    
        1. If the appropriate option is raised, run script to update the input/output paths.
        2. If the appropriate option is raised, run script to update the config file.
        3. Initialise the :obj:`parsing.load` module which automatically parses the files at
           the specified paths.
        4. Unless construction is disabled, call appropriate construction scripts and receive
           Python representation of all the calibrations, TM-packets, TC-commands, etc. that
           occur in the parsed files.
        5. Perform some checks that these objects (mainly TM-packets and calibrations) are linked
           in a correct way.
        6. Unless generation is disabled, call the generation script which turns all previously
           constructed objects into MIB tables and saves them.
        7. If the appropriate option is raised, show the parsed files' contents in a GUI visualisation.
        
    Args:
        visual (bool): ``True`` if the GUI visualisation of the parsed files should be shown, ``False`` otherwise (and by 
            default).
        generate (bool): ``True`` (by default) if the MIB tables should be generated and saved from the constructed 
            Python representations, ``False`` otherwise.
        parseonly (bool): ``True`` if only parsing of the C-files should be done and none of the subsequent steps. 
            ``False`` otherwise and by default.
        paths (bool): ``True`` if the script to update the input/output paths should be run, ``False`` otherwise (and by
            default).
        config (bool): ``True`` if the script to update the config file should be run, ``False`` otherwise (and by default).
        
    Returns:
        bool: ``True`` if the script finished successfully, ``None`` otherwise. 
    """
    if paths:
        import utilities.update as update

        update.update_path()
    if config:
        import utilities.update as update

        update.update_config()

    tm_lis = []
    tc_lis = []
    import parsing.load as load

    if not parseonly:
        # creating TM-packets
        import construction.calib as calib
        import construction.TM_packet as tm_packet
        import construction.TM_packet_methods as tm_packet_methods

        cal1 = calib.calib_extract(load.TmH.comments)
        cal2 = calib.calib_extract(load.TcTmH.comments)
        cal = {i: cal1[i] + cal2[i] for i in cal1}
        TmHead = tm_packet.TM_header(load.TmH)
        for i in load.TmC.structures[1].elements:
            matched = tm_packet_methods.header_search(i.entries[".type"])
            for k in matched:
                pack = tm_packet.TM_packet(i, k, TmHead)
                calib.cur_update(pack, cal)
                tm_lis.append(pack)

        # creating TC-packets
        import construction.TC_packet as tc_packet
        import construction.TC_packet_methods as tc_packet_methods

        dec1 = calib.decal_extract(load.TcH.comments)
        dec2 = calib.decal_extract(load.TcTmH.comments)
        dec = dec1 + dec2
        ver1 = calib.verif_extract(load.TcH.comments)
        ver2 = calib.verif_extract(load.TcTmH.comments)
        ver = ver1+ver2
        TcHead = tc_packet.TC_header(tc_packet_methods.find_header(load.TcH))
        packets = tc_packet_methods.packet_search(load.TcH)
        for i in packets:
            comm = tc_packet.TC_packet(i, TcHead)
            calib.cpc_update(comm, dec)
            calib.cvs_update(comm, ver)
            tc_lis.append(comm)

        if generate:
            import generation.gener as gener

            gener.generation_hub(tm_lis, tc_lis, cal, dec, ver, TcHead)
    if visual:
        try:
            import utilities.visualiser as visualiser

            visualiser.main([load.TmH, load.TcTmH, load.TmC, load.TcH])
        except ModuleNotFoundError:
            print(
                "Warn.:\tPySide6 not found. Please install it in order to show the parsed files."
            )
    return True


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
    parser.add_argument(
        "-p",
        "--update_paths",
        help="start by running script to update paths and store them in the json5 file",
        action="store_true",
    )
    parser.add_argument(
        "-c",
        "--update_config",
        help="start by running script to update config parameters (stored in json5 file)",
        action="store_true",
    )
    arguments = parser.parse_args()
    main(
        arguments.visualise,
        not arguments.xgenerate,
        arguments.onlyparse,
        arguments.update_paths,
        arguments.update_config,
    )
