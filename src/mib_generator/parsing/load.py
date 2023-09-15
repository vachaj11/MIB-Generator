"""Central location from which other modules can source data from the parsed C-files.

This module is initialised and its methods are called in the first step of the MIB construction process. At this point the C-files
are loaded from the defined paths, are parsed using the :obj:`mib_generator.parsing.parser_main.main` method and are
subsequently available for other scripts throughout the rest of the MIB construction process. The only other
method here is :obj:`extr_values` which serves the purpose creating a global evaluation dictionary holding
values from all header enums, macros, etc...

Attributes:
    TmH (list): Holds the Python parsed representation of the Tm-header C-files. Each of type 
        :obj:`mib_generator.parsing.parser_main.file`
    TcH (list): Holds the Python parsed representation of the Tc-header C-files. Each of type 
        :obj:`mib_generator.parsing.parser_main.file`
    TcTmH (list): Holds the Python parsed representation of the TcTm-header C-files. Each of type 
        :obj:`mib_generator.parsing.parser_main.file`
    TmC (list): Holds the Python parsed representation of the Tm (normal) C-files. Each of type 
        :obj:`mib_generator.parsing.parser_main.file`
    enumerations (dict): A dictionary containing all possible usable evaluations/enumerations sourced 
        form enums, macros, etc... found in all 3 of the parsed header files.
"""
import os

import json5

import mib_generator.data.warn as warn
import mib_generator.parsing.parser_main as par

TmC_path = ""
TmH_path = ""
TcH_path = ""
TcTmH_path = ""
out_dir = ""
out_doc = ""

conf = ""

TmH = None
TcH = None
TcTmH = None
TmC = None

enumerations = {}


def get_paths():
    """Load paths from the temporary config files.

    This method looks up paths to each of the input files in the config files in the runtime config directory.
    It then saves these paths as global attributes of the :obj:`mib_generator.parsing.load` module, so they can
    be easily accessed to other methods in the whole program.
    """
    try:
        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "temp", "paths.json5"
        )
        file = open(file_path, "r")
        paths = json5.load(file)
        file.close()
        tmc = paths["TmFile"]
        globals()["TmC_path"] = tmc if type(tmc) is list else [tmc]
        tmh = paths["TmHeader"]
        globals()["TmH_path"] = tmh if type(tmh) is list else [tmh]
        tch = paths["TcHeader"]
        globals()["TcH_path"] = tch if type(tch) is list else [tch]
        tctmh = paths["TcTmHeader"]
        globals()["TcTmH_path"] = tctmh if type(tctmh) is list else [tctmh]
        globals()["out_dir"] = paths["OutDir"]
        globals()["out_doc"] = paths["OutDoc"]
    except:
        warn.raises("EPL1")


def get_conf():
    try:
        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "temp", "config.json5"
        )
        fil = open(file_path, "r")
        globals()["conf"] = json5.load(fil)
        fil.close()
    except:
        globals()[""] = {}


def parse_all():
    """Parse the inputted C-files and save the output.

    This method uses the :obj:`mib_generator.parsing.parser_main` module to parse contents of the files specified
    at the paths given by global attributes of this module. It then assigns the outputs of the parsing process to
    various other global attributes of this module, so they can be easily accessed.
    """
    try:
        globals()["TmH"] = [par.main(i) for i in TmH_path]
    except:
        warn.raises("EPL2", "Tm .h")
    try:
        globals()["TcH"] = [par.main(i) for i in TcH_path]
    except:
        warn.raises("EPL2", "Tc .h")
    try:
        globals()["TcTmH"] = [par.main(i) for i in TcTmH_path]
    except:
        warn.raises("EPL2", "TcTm .h")
    try:
        globals()["TmC"] = [par.main(i) for i in TmC_path]
    except:
        warn.raises("EPL2", "Tm .c")


def enum_stuff():
    """Create a dictionary that includes all the possible evaluations from the input files.

    For each of the inputted (and processed) C-files, this method extracts an evaluation (dictionary
    including all possible variable substitutions, from e.g. `enum` objects.) and then joins all of
    these dictionaries to one and assigns it to a global variable so it can be easily accessed.
    """
    try:
        enum1 = extr_values(TmH)
        enum2 = extr_values(TcTmH)
        enum3 = extr_values(TcH)
        globals()["enumerations"] = enum1 | enum2 | enum3
    except:
        warn.raises("WPL1")


def extr_values(files):
    """Create a dictionary from constants, ``enum`` correspondences, etc... in the given files.

    Goes through all objects in the parsed files and for each ``enum`` and macro, appends the name-value
    pairs present to a dictionary (which represents the "global" evaluation in the file).

    Args:
        files (list): Files from which the evaluation dictionary is to be extracted. Each of type
            :obj:`mib_generator.parsing.parser_main.file`

    Returns:
        dict: A dictionary with all possible "global" evaluation found in the given file.
    """
    lis = {}
    if files:
        for x in [a for file in files for a in file.structures]:
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


def load_all():
    """Run all initialisation and parsing methods.

    This method (replacing previous simple initialisation of this module) runs other methods, which

        1. Load the paths to input C-files.
        2. Load the configuration settings.
        2. Parse files at these paths.
        3. Create evaluation dictionary from these parsed files.
    """
    get_paths()
    get_conf()
    parse_all()
    enum_stuff()
