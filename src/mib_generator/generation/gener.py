"""This module serves the purpose of generating MIB databases from inputed objects and checking their validity.

Methods in this module generate MIB databases from their representations previously generated by the
:obj:`mib_generator.construction` package/modules and run finals checks on the results to ensure that the outputted tables/MIB files 
adhere to the requirements on the type, length, uniqueness and "mandatoriness".
"""

import mib_generator.data.warn as warn
import mib_generator.generation.gener_methods as gm
import mib_generator.parsing.load as load


def generation_hub(
    Tm_packets=None,
    Tc_packets=None,
    calibrations=None,
    decalibrations=None,
    verifications=None,
    Tc_head=None,
    cfg=None,
):
    """Take all constructed packets/calibrations/commands and call generation scripts for each table.

    This method is the "main interface" for the generation process. It is passed various objects which have MIB tables
    associated to them and for each of them calls the appropriate generation methods (either :obj:`one_generate` for objects
    which have only one row of the given MIB table associated to them or :obj:`two_generate` in case of possibly multiple
    rows) with the correct parameters.

    What tables are generated is determined by the contents of the ``../data/config.json5`` config file, or it can be overridden
    using the :obj:`cfg` argument. Because of this optionality, none of the arguments of this method are compulsory, since they
    are not needed for generation of some tables, which is what this method could be asked to do. However they have to be present
    if a table which is based on them is to be generated.

    Args:
        Tm_packets (list): List of TM-packets (their Python representations), each represented by an object of type
            :obj:`mib_generator.construction.TM_packet.TM_packet`.
        Tc_packets (list): List of TC-commands (their Python representations), each represented by an object of type
            :obj:`mib_generator.construction.TC_packet.TC_packet`.
        calibrations (dict): Dictionary holding lists various calibrations (their Python representations), each calibration
            being an object of some child-class of :obj:`mib_generator.construction.calib.calib`.
        decalibrations (list): List of textual decalibrations (their Python representations), each represented by an object of
            type :obj:`mib_generator.construction.calib.decalib`.
        verifications (list): List of TC-command verifications (their Python representations), each represented by an object of
            type :obj:`mib_generator.construction.calib.verification`.
        Tc_head (construction.TC_packet.TC_header): A header included in all TC-commands.
        cfg (list): List of names of the MIB tables to be generated. Otherwise a default list stated in the config file is used.

    Returns:
        dict: A dictionary holding all the generated mib tables (in form of Python 2D lists) with their names as keys.
    """
    if cfg is None:
        to_be = load.conf["mib"]
    else:
        to_be = cfg

    tables = {}
    for i in to_be:
        if i in {"mcf", "lgf", "txf", "txp", "caf", "cap"}:
            if calibrations is not None:
                tables[i] = cal_gen(i, calibrations)
            else:
                warn.raises("WGG1", i)
        elif i in {"pid", "pic", "tpcf", "pcf", "plf", "cur", "vpd"}:
            if Tm_packets is not None:
                tables[i] = Tmp_gen(i, Tm_packets)
            else:
                warn.raises("WGG1", i)
        elif i in {"ccf", "cpc", "cdf", "prf", "prv", "cvp"}:
            if Tc_packets is not None:
                tables[i] = Tcp_gen(i, Tc_packets)
            else:
                warn.raises("WGG1", i)
        elif i in {"tcp", "pcpc", "pcdf"}:
            if Tc_head is not None:
                tables[i] = Tch_gen(i, [Tc_head])
            else:
                warn.raises("WGG1", i)
        elif i in {"paf", "pas"}:
            if decalibrations is not None:
                tables[i] = dec_gen(i, decalibrations)
            else:
                warn.raises("WGG1", i)
        elif i in {"cvs"}:
            if verifications is not None:
                tables[i] = ver_gen(i, verifications)
            else:
                warn.raises("WGG1", i)
        else:
            warn.raises("WGG2", i)

    return tables


def save_tables(tables):
    """Reformat and save mib tables in the passed dictionary.

    Goes through the passed dictionary holding mib tables and for each first reformats it into an appropriate ASCII string and then
    saves it to the specified folder with all mib tables.

    Args:
        tables (dict): A dictionary containing mib tables in the form of 2D Python lists as values with their names as keys.
    """
    for i in tables:
        mib = gm.list_to_mib(tables[i])
        gm.save_mib(mib, i)


def cal_gen(typ, calibrations):
    """Choose how the given calibration MIB table should be constructed and construct it.

    Based on its name, this function chooses what method to call in order to generate and check the given table. It then
    calls this method and returns the result.

    Args:
        typ (str): Name of the MIB table to be generated.
        calibrations (list): List of dictionaries of calibrations from which the table is to be constructed. Each calibration
            is of some type which is a child-class of :obj:`mib_generator.construction.calib.calib`.

    Returns:
        list: A 2D list (list of lists) representing the outputted MIB table (still in Python format).
    """
    match typ:
        case "mcf":
            return gm.one_generate(calibrations["mcfs"], "mcf")
        case "lgf":
            return gm.one_generate(calibrations["lgfs"], "lgf")
        case "txf":
            return gm.one_generate(calibrations["txfs"], "txf")
        case "txp":
            return gm.two_generate(calibrations["txfs"], "txp")
        case "caf":
            return gm.one_generate(calibrations["cafs"], "caf")
        case "cap":
            return gm.two_generate(calibrations["cafs"], "cap")


def Tmp_gen(typ, Tm_packets):
    """Choose how the given Tm-packet MIB table should be constructed and construct it.

    Based on its name, this function chooses what method to call in order to generate and check the given table. It then
    calls this method and returns the result.

    The special case here is with respect to the pic table in case of which, first a filter on the packet list have to be run
    since the entries in the pic table are a subset of those in pid/list of packages and hence otherwise false warning would
    be raised later (due to lack of uniqueness).

    Args:
        typ (str): Name of the MIB table to be generated.
        Tm_packets (list): List of Tm-packets from which the table is to be constructed. Each of type
            :obj:`mib_generator.construction.TM_packet.TM_packet`.

    Returns:
        list: A 2D list (list of lists) representing the outputted MIB table (still in Python format).
    """
    match typ:
        case "pid":
            return gm.one_generate(Tm_packets, "pid")
        case "pic":
            # the infamous pic filter
            pic_packets = gm.pic_filter(Tm_packets)
            return gm.one_generate(pic_packets, "pic")
        case "tpcf":
            return gm.one_generate(Tm_packets, "tpcf")
        case "pcf":
            gm.mnemon_check(Tm_packets, "pcf")
            return gm.two_generate(Tm_packets, "pcf")
        case "plf":
            return gm.two_generate(Tm_packets, "plf")
        case "cur":
            return gm.two_generate(Tm_packets, "cur")
        case "vpd":
            return gm.two_generate(Tm_packets, "vpd")


def Tcp_gen(typ, Tc_packets):
    """Choose how the given Tc-packet MIB table should be constructed and construct it.

    Based on its name, this function chooses what method to call in order to generate and check the given table. It then
    calls this method and returns the result.

    Args:
        typ (str): Name of the MIB table to be generated.
        Tc_packets (list): List of Tc-packets from which the table is to be constructed. Each of type
            :obj:`mib_generator.construction.TC_packet.TC_packet`.

    Returns:
        list: A 2D list (list of lists) representing the outputted MIB table (still in Python format).
    """
    match typ:
        case "ccf":
            gm.mnemon_check(Tc_packets, "ccf")
            return gm.one_generate(Tc_packets, "ccf")
        case "cpc":
            gm.mnemon_check(Tc_packets, "cpc")
            return gm.two_generate(Tc_packets, "cpc")
        case "cdf":
            return gm.two_generate(Tc_packets, "cdf")
        case "prf":
            return gm.two_generate(Tc_packets, "prf")
        case "prv":
            return gm.two_generate(Tc_packets, "prv")
        case "cvp":
            return gm.two_generate(Tc_packets, "cvp")


def Tch_gen(typ, Tc_head):
    """Choose how the given Tc-header MIB table should be constructed and construct it.

    Based on its name, this function chooses what method to call in order to generate and check the given table. It then
    calls this method and returns the result.

    Args:
        typ (str): Name of the MIB table to be generated.
        Tc_head (list): List of Tc-headers from which the table is to be constructed. Each of type
            :obj:`mib_generator.construction.TC_packet.TC_header`.

    Returns:
        list: A 2D list (list of lists) representing the outputted MIB table (still in Python format).
    """
    match typ:
        case "tcp":
            return gm.one_generate(Tc_head, "tcp")
        case "pcpc":
            return gm.two_generate(Tc_head, "pcpc")
        case "pcdf":
            return gm.two_generate(Tc_head, "pcdf")


def dec_gen(typ, decalibrations):
    """Choose how the given decalibration MIB table should be constructed and construct it.

    Based on its name, this function chooses what method to call in order to generate and check the given table. It then
    calls this method and returns the result.

    Args:
        typ (str): Name of the MIB table to be generated.
        decalibrations (list): List of decalibrations from which the table is to be constructed. Each of type
            :obj:`mib_generator.construction.calib.decalib`.

    Returns:
        list: A 2D list (list of lists) representing the outputted MIB table (still in Python format).
    """
    match typ:
        case "paf":
            return gm.one_generate(decalibrations, "paf")
        case "pas":
            return gm.two_generate(decalibrations, "pas")


def ver_gen(typ, verifications):
    """Choose how the given verification MIB table should be constructed and construct it.

    Based on its name, this function chooses what method to call in order to generate and check the given table. It then
    calls this method and returns the result.

    Args:
        typ (str): Name of the MIB table to be generated.
        verifications (list): List of verifications from which the table is to be constructed. Each of type
            :obj:`mib_generator.construction.calib.verification`.

    Returns:
        list: A 2D list (list of lists) representing the outputted MIB table (still in Python format).
    """
    match typ:
        case "cvs":
            return gm.one_generate(verifications, "cvs")
