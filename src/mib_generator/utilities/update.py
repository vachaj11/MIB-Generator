"""Various CLI scripts that update various files that configure the generation process.

This module holds methods that allow the user to easily modify various files that affects the behaviour of the main Python
script. They can be called by simply importing and calling them or through appropriate flags build into the main CLI of the 
MIB generator.  
"""
import os

import json5

import mib_generator.data.warn as warn


def update_path(directory=None):
    """Run a series of queries asking user to specify valid paths to input files.

    This method allows the user to specify paths to the 4 input files and 1 output directory that the MIB generator requires.
    The previously stored values are shown to the user and he can leave them be or choose to modify them stating the location of
    the target files either in terms of absolute or relative path. The inputted location is then checked and if it exists, then
    the path is saved (in absolute form). Only existence is checked, not that the file is valid for the given purpose.

    All of this happens with respect to either a paths config file specified through the passed ``directory`` parameter or
    w.r.t. the default paths config file which is located in :obj:`mib_generator.data`.

    Args:
        directory (str): String with the location of the directory in which the paths config file to be modified is located.
    """
    if not directory:
        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "paths.json5"
        )
    else:
        file_path = os.path.join(directory, "paths.json5")
    if os.path.isfile(file_path):
        fil = open(file_path, "r")
        leg_data = json5.load(fil)
        fil.close()
    else:
        leg_data = {}
        for i in ["TmHeader", "TcTmHeader", "TmFile", "TcHeader", "OutDir", "OutDoc"]:
            leg_data[i] = "TO BE INPUTTED"
    data = {}
    valid_TmH = False
    print("The current absolute path is: " + os.getcwd())
    print("------")
    while not valid_TmH:
        pre_val = leg_data["TmHeader"]
        if type(pre_val) is list:
            pre_val = pre_val[0]
        print("State relative or absolute path to Tm Header file.")
        print(
            "(Inputting multiple paths for one file is not supported in the UI script, use the GUI for that purpose)"
        )
        print("Currently this path is: " + pre_val)
        print("(press Enter if you want to keep this value)")
        path = input("Path: ")
        if path == "" and os.path.isfile(pre_val):
            data["TmHeader"] = [pre_val]
            valid_TmH = True
        elif os.path.isfile(path):
            data["TmHeader"] = [os.path.abspath(path)]
            valid_TmH = True
        else:
            print("Error:\tFailed to find the specified file, try again.")
        print("------")
    valid_TcTmH = False
    while not valid_TcTmH:
        pre_val = leg_data["TcTmHeader"]
        if type(pre_val) is list:
            pre_val = pre_val[0]
        print("State relative or absolute path to TcTm Header file.")
        print(
            "(Inputting multiple paths for one file is not supported in the UI script, use the GUI for that purpose)"
        )
        print("Currently this path is: " + pre_val)
        print("(press Enter if you want to keep this value)")
        path = input("Path: ")
        if path == "" and os.path.isfile(pre_val):
            data["TcTmHeader"] = [pre_val]
            valid_TcTmH = True
        elif os.path.isfile(path):
            data["TcTmHeader"] = [os.path.abspath(path)]
            valid_TcTmH = True
        else:
            print("Error:\tFailed to find the specified file, try again.")
        print("------")
    valid_TmC = False
    while not valid_TmC:
        pre_val = leg_data["TmFile"]
        if type(pre_val) is list:
            pre_val = pre_val[0]
        print("State relative or absolute path to Tm C file.")
        print(
            "(Inputting multiple paths for one file is not supported in the UI script, use the GUI for that purpose)"
        )
        print("Currently this path is: " + pre_val)
        print("(press Enter if you want to keep this value)")
        path = input("Path: ")
        if path == "" and os.path.isfile(pre_val):
            data["TmFile"] = [pre_val]
            valid_TmC = True
        elif os.path.isfile(path):
            data["TmFile"] = [os.path.abspath(path)]
            valid_TmC = True
        else:
            print("Error:\tFailed to find the specified file, try again.")
        print("------")
    valid_TcH = False
    while not valid_TcH:
        pre_val = leg_data["TcHeader"]
        if type(pre_val) is list:
            pre_val = pre_val[0]
        print("State relative or absolute path to Tc Header file.")
        print(
            "(Inputting multiple paths for one file is not supported in the UI script, use the GUI for that purpose)"
        )
        print("Currently this path is: " + pre_val)
        print("(press Enter if you want to keep this value)")
        path = input("Path: ")
        if path == "" and os.path.isfile(pre_val):
            data["TcHeader"] = [pre_val]
            valid_TcH = True
        elif os.path.isfile(path):
            data["TcHeader"] = [os.path.abspath(path)]
            valid_TcH = True
        else:
            print("Error:\tFailed to find the specified file, try again.")
        print("------")
    valid_Out = False
    while not valid_Out:
        print("State relative or absolute path to the output directory.")
        print("Currently this path is: " + str(leg_data["OutDir"]))
        print("(press Enter if you want to keep this value)")
        path = input("Path: ")
        if path == "" and os.path.isdir(leg_data["OutDir"]):
            data["OutDir"] = leg_data["OutDir"]
            valid_Out = True
        elif os.path.isdir(path):
            data["OutDir"] = os.path.abspath(path)
            valid_Out = True
        else:
            print("Error:\tFailed to find the specified directory, try again.")
        print("------")
    valid_Doc = False
    while not valid_Doc:
        print("State relative or absolute path to the docx output file.")
        print("Currently this path is: " + str(leg_data["OutDoc"]))
        print("(press Enter if you want to keep this value)")
        path = input("Path: ")
        if path == "" and os.path.isdir(os.path.dirname(leg_data["OutDoc"])):
            data["OutDoc"] = leg_data["OutDoc"]
            valid_Doc = True
        elif os.path.isdir(os.path.dirname(path)):
            data["OutDoc"] = os.path.abspath(path)
            valid_Doc = True
        else:
            print(
                "Error:\tFailed to find the specified directory into which the file should be placed, try again."
            )
        print("------")
    valid_Xls = False
    while not valid_Xls:
        print("State relative or absolute path to the xls output file.")
        print("Currently this path is: " + str(leg_data["OutXls"]))
        print("(press Enter if you want to keep this value)")
        path = input("Path: ")
        if path == "" and os.path.isdir(os.path.dirname(leg_data["OutXls"])):
            data["OutXls"] = leg_data["OutXls"]
            valid_Xls = True
        elif os.path.isdir(os.path.dirname(path)):
            data["OutXls"] = os.path.abspath(path)
            valid_Xls = True
        else:
            print(
                "Error:\tFailed to find the specified directory into which the file should be placed, try again."
            )
        print("------")
    fil = open(file_path, "w")
    fil.write("// This file stores various paths to source/output files\n")
    fil.write(json5.dumps(data))
    fil.close()
    print("======")


def update_config_d(directory=None):
    """Run a series of queries asking user to specify parsing configuration parameters.

    This method allows the user to specify configuration parameters to be used by the parsing pre-processor (i.e. say,
    whether the macro is defined or not). First, the already saved parameters are loaded and the user is asked whether
    he wants to keep the current value, change it or delete the parameter altogether. Then, the user is given the option
    to create a new parameter. The only valid accepted of parameters are boolean or a string.

    All of this happens with respect to either a config file specified through the passed ``directory`` parameter or
    w.r.t. the default config file which is located in :obj:`mib_generator.data`.

    Args:
        directory (str): String with the location of the directory in which the config file to be modified is located.
    """
    if not directory:
        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "config.json5"
        )
    else:
        file_path = os.path.join(directory, "config.json5")
    if os.path.isfile(file_path):
        fil = open(file_path, "r")
        leg_fil = json5.load(fil)
        fil.close()
        if "def" in leg_fil.keys():
            leg_data = leg_fil["def"]
        else:
            leg_data = {}
    else:
        leg_fil = {}
        leg_data = {}
    data = {}
    print("To change the pre-processor config parameters:")
    print('Write "True" to set the parameter to True (marking it as defined).')
    print('Write "False" to set the parameter to False (marking it as undefined).')
    print(
        'Write "DEL" to delete this parameter (which will mean it is undefined if asked).'
    )
    print(
        "Write anything else to store that value as a string (non-empty string will mean defined)."
    )
    print("Leave the input field blank to leave the value unchanged.")
    print("------")

    for i in leg_data:
        print(
            "Set value of parameter "
            + i
            + ", which is currently set to "
            + str(leg_data[i])
            + "."
        )
        x = input("Input: ")
        if x == "True":
            data[i] = True
        elif x == "False":
            data[i] = False
        elif x == "DEL":
            pass
        elif x == "":
            data[i] = leg_data[i]
        else:
            data[i] = x
        print("------")
    additional = True
    while additional:
        print(
            "If you want to add additional parameter, input parameter name (otherwise leave the field blank)."
        )
        y = input("Input: ")
        if not y:
            additional = False
        else:
            print("Set value of this parameter " + y + " (as above).")
            x = input("Input: ")
            if x == "True":
                data[y] = True
            elif x == "False":
                data[y] = False
            elif x == "DEL":
                pass
            elif x == "":
                data[y] = ""
            else:
                data[y] = x
            print("------")

    fil = open(file_path, "w")
    fil.write("// This file stores various definitions used mainly by the parser\n")
    leg_fil["def"] = data
    fil.write(json5.dumps(leg_fil))
    fil.close()
    print("======")


def update_config_m(directory=None):
    """Run a series of queries asking user to specify generation configuration parameters.

    This method allows the user to specify configuration parameters to be used at the generation step (i.e. the list of the MIB
    databases to be generated). First, the already saved parameters are loaded and the user is asked whether
    he wants to keep, change or delete them. Then, the user is given the option
    to create a new parameter. The only valid accepted of parameters are strins.

    All of this happens with respect to either a config file specified through the passed ``directory`` parameter or
    w.r.t. the default config file which is located in :obj:`mib_generator.data`.

    Args:
        directory (str): String with the location of the directory in which the config file to be modified is located.
    """
    if not directory:
        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "config.json5"
        )
    else:
        file_path = os.path.join(directory, "config.json5")
    if os.path.isfile(file_path):
        fil = open(file_path, "r")
        leg_fil = json5.load(fil)
        fil.close()
        if "mib" in leg_fil.keys():
            leg_data = leg_fil["mib"]
        else:
            leg_data = []
    else:
        leg_data = []
    data = []
    print("To change the generation config parameters:")
    print('Write "del" (or similar) to delete the parameter.')
    print('Write anything else (including "") to keep it.')
    print("------")
    print("The currently saved parameters (mib tables to be generated) are:")
    for i in leg_data:
        x = input('The parameter "' + i + '". Keep it? ')
        if x in {"del", "Del", "DEL", "delete", "Delete", "DELETE"}:
            print('The parameter "' + i + '" was deleted')
        else:
            data.append(i)
    print("------")
    additional = True
    while additional:
        print(
            "If you want to add additional parameter, input parameter name (otherwise leave the field blank)."
        )
        y = input("Input: ")
        if y:
            data.append(y)
            print('Parameter "' + y + '" added.')
        else:
            additional = False

    fil = open(file_path, "w")
    fil.write("// This file stores various definitions used mainly by the parser\n")
    leg_fil["mib"] = data
    fil.write(json5.dumps(leg_fil))
    fil.close()
    print("======")


def update_config_n(directory=None):
    """Run a series of queries asking user to specify parameter name creation configuration parameters.

    This method allows the user to specify configuration parameters to be used at the parameter construction step (i.e.
    what form should the names of the parameters take. There are four parameters which define these settings and the user
    is asked about the value of each of them which he can either change or leave the previous.

    All of this happens with respect to either a config file specified through the passed ``directory`` parameter or
    w.r.t. the default config file which is located in :obj:`mib_generator.data`.

    Args:
        directory (str): String with the location of the directory in which the config file to be modified is located.
    """
    if not directory:
        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "config.json5"
        )
    else:
        file_path = os.path.join(directory, "config.json5")
    if os.path.isfile(file_path):
        fil = open(file_path, "r")
        leg_fil = json5.load(fil)
        fil.close()
        if "nam" in leg_fil.keys():
            leg_data = leg_fil["nam"]
        else:
            leg_data = {}
    else:
        leg_data = {}

    data = {}
    print("To change a construction config parameter:")
    print("Write anything to save it as the parameter's value.")
    print("(assuming it is appropriatelly string or int)")
    print("Write nothing (press Enter) to keep the previous value.")
    print('Write "---" to save "" as the parameter\'s value (where appropriate).')
    print("------")
    print('Parameter - Numerical index length in "PCF_NAME".')
    print("(integer < 6 expected)")
    try:
        print("Current value is: " + str(leg_data["pcf"]))
        pre = leg_data["pcf"]
    except:
        print("There is no current value.")
        pre = None
    fin = False
    while not fin:
        x = input("Set a value for this parameter: ")
        if not x:
            out = pre
        else:
            try:
                out = int(x)
            except:
                out = None
        if out in range(6):
            data["pcf"] = out
            fin = True
        else:
            print("Invalid value entered.")
    print("------")
    print('Parameter - Numerical index length in "CPC_PNAME".')
    print("(integer < 6 expected)")
    try:
        print("Current value is: " + str(leg_data["cpc"]))
        pre = leg_data["cpc"]
    except:
        print("There is no current value.")
        pre = None
    fin = False
    while not fin:
        x = input("Set a value for this parameter: ")
        if not x:
            out = pre
        else:
            try:
                out = int(x)
            except:
                out = None
        if out in range(6):
            data["cpc"] = out
            fin = True
        else:
            print("Invalid value entered.")
    print("------")
    print('Parameter - Default "nature" value for "PCF_NAME".')
    print("(str with len() < 2 expected)")
    try:
        print("Current value is: " + str(leg_data["nat_pcf"]))
        pre = leg_data["nat_pcf"]
    except:
        print("There is no current value.")
        pre = None
    fin = False
    while not fin:
        x = input("Set a value for this parameter: ")
        if not x:
            out = pre
        else:
            if x == "---":
                out = ""
            else:
                out = x
        if len(out) < 2:
            data["nat_pcf"] = out
            fin = True
        else:
            print("Invalid value entered.")
    print("------")
    print('Parameter - Default "nature" value for "CPC_PNAME".')
    print("(str with len() < 2 expected)")
    try:
        print("Current value is: " + str(leg_data["nat_cpc"]))
        pre = leg_data["nat_cpc"]
    except:
        print("There is no current value.")
        pre = None
    fin = False
    while not fin:
        x = input("Set a value for this parameter: ")
        if not x:
            out = pre
        else:
            if x == "---":
                out = ""
            else:
                out = x
        if len(out) < 2:
            data["nat_cpc"] = out
            fin = True
        else:
            print("Invalid value entered.")
    print("------")
    fil = open(file_path, "w")
    fil.write("// This file stores various definitions used mainly by the parser\n")
    leg_fil["nam"] = data
    fil.write(json5.dumps(leg_fil))
    fil.close()
    print("======")
