"""This module works as a startpoint and a junction for creation of the MIB databases.

This module through its :obj:`main` method serves the role of a logical centre of the whole program. It interchanges
appropriate files between sub-packages, calls appropriate methods for each task, etc. See :obj:`main` for more info.
"""


def main(visual=False, generate=True, parseonly=False, paths=False, config=False, generate_t=False):
    """Run this whole hellish thing.

    This method holds the main logic of the whole program. Roughly it sequentially does this:

        1. If the appropriate option is raised, run script to update the input/output paths.
        2. If the appropriate option is raised, run script to update the config file.
        3. Initialise the :obj:`mib_generator.parsing.load` module which automatically parses the files at
           the specified paths.
        4. Unless construction is disabled, call appropriate construction scripts and receive
           Python representation of all the calibrations, TM-packets, TC-commands, etc. that
           occur in the parsed files.
        5. Perform some checks that these objects (mainly TM-packets and calibrations) are linked
           in a correct way.
        6. Unless generation is disabled, call the generation script which turns all previously
           constructed objects into MIB tables and saves them.
        7. If the appropriate option is raised, generate a document summing up the interpreted TM/TC packages.
        8. If the appropriate option is raised, show the parsed files' contents in a GUI visualisation.

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
        import mib_generator.utilities.update as update

        update.update_path()
    if config:
        import mib_generator.utilities.update as update

        update.update_config_d()
        update.update_config_m()

    tm_lis = []
    tc_lis = []
    import mib_generator.parsing.load as load

    if not parseonly:
        # creating TM-packets
        import mib_generator.construction.calib as calib
        import mib_generator.construction.TM_packet as tm_packet
        import mib_generator.construction.TM_packet_methods as tm_packet_methods

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
        import mib_generator.construction.TC_packet as tc_packet
        import mib_generator.construction.TC_packet_methods as tc_packet_methods

        dec1 = calib.decal_extract(load.TcH.comments)
        dec2 = calib.decal_extract(load.TcTmH.comments)
        dec = dec1 + dec2
        ver1 = calib.verif_extract(load.TcH.comments)
        ver2 = calib.verif_extract(load.TcTmH.comments)
        ver = ver1 + ver2
        TcHead = tc_packet.TC_header(tc_packet_methods.find_header(load.TcH))
        packets = tc_packet_methods.packet_search(load.TcH)
        for i in packets:
            comm = tc_packet.TC_packet(i, TcHead)
            calib.cpc_update(comm, dec)
            calib.cvs_update(comm, ver)
            tc_lis.append(comm)

        if generate:
            import mib_generator.generation.gener as gener

            gener.generation_hub(tm_lis, tc_lis, cal, dec, ver, TcHead)
            
        if generate_t:
            import mib_generator.generation.gener_doc as generd
            
            generd.gen_doc(tm_lis, tc_lis)
    if visual:
        try:
            import mib_generator.utilities.visualiser as visualiser

            visualiser.main([load.TmH, load.TcTmH, load.TmC, load.TcH])
        except ModuleNotFoundError:
            print(
                "Warn.:\tPySide6 not found. Please install it in order to show the parsed files."
            )
    return True
