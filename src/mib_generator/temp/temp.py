"""This module holds method/s which take care of transferring the correct config files into the runtime directory.
"""
import os
import shutil

import json5

import mib_generator.data.warn as warn


def move_conf(dire=None):
    """Transfer the config files from the specified directory to runtime location.

    This method looks at the passed directory, checks what config files are inside it and if such are found, moves them
    to the package runtime directory (:obj:`mib_generator.temp`), rewriting config files which might have been there already.
    If some config file is not found in the specified directory, transfers config from the default directory
    (:obj:`mib_generator.data`) instead.

    Args:
        dire (str): A string specifying the directory from which the config files are to be taken.
    """
    here = os.path.dirname(__file__)
    data = os.path.join(os.path.dirname(here), "data")
    if dire and os.path.isfile(os.path.join(dire, "paths.json5")):
        source_p = os.path.join(dire, "paths.json5")
    else:
        source_p = os.path.join(data, "paths.json5")
    shutil.copy(source_p, here)
    if dire and os.path.isfile(os.path.join(dire, "config.json5")):
        source_c = os.path.join(dire, "config.json5")
    else:
        source_c = os.path.join(data, "config.json5")
    shutil.copy(source_c, here)
    
def evom_conf(dire):
    here = os.path.dirname(__file__)
    temp = os.path.join(os.path.dirname(here), "temp")
    if os.path.isdir(dire):
        shutil.copy(os.path.join(temp, "config.json5"),os.path.join(dire, "config.json5"))
        shutil.copy(os.path.join(temp, "paths.json5"),os.path.join(dire, "paths.json5"))
    
def update_paths(diction):
    file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "temp", "paths.json5"
    )
    try:
        fil = open(file_path, "r")
        leg_data = json5.load(fil)
        fil.close()
    except:
        leg_data = {}
    for i in diction:
        if os.path.isfile(diction[i]) or os.path.isdir(diction[i]):
            pass
        else:
            if i in leg_data.keys():
                F = os.path.isfile(leg_data[i])
                D = os.path.isdir(leg_data[i])
                if F or D:
                    warn.raises("WTT1",diction[i], i, leg_data[i])
                else:
                    warn.raises("WTT2", diction[i], i)
            else:
                warn.raises("WTT2", diction[i], i)
    
    fil = open(file_path, "w")
    fil.write("// This file stores various paths to source/output files\n")
    fil.write(json5.dumps(diction))
    fil.close()
    return diction
    
def fetch_paths():
    file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "temp", "paths.json5"
    )
    try:
        fil = open(file_path, "r")
        leg_data = json5.load(fil)
        fil.close()
    except:
        leg_data = {}
    return leg_data
            
