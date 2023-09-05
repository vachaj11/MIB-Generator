"""
config goes here at runtime
"""
import os
import shutil

def move_conf(dire):
    here = os.path.dirname(__file__)
    data = os.path.join(os.path.dirname(here),"data")
    if dire and os.path.isfile(os.path.join(dire, "paths.json5")):
        source_p = os.path.join(dire,"paths.json5")
    else:
        source_p = os.path.join(data,"paths.json5")
    shutil.copy(source_p, here)
    if dire and os.path.isfile(os.path.join(dire, "config.json5")):
        source_c = os.path.join(dire,"config.json5")
    else:
        source_c = os.path.join(data,"config.json5")
    shutil.copy(source_c, here)
