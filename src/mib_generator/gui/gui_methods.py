import json5
import os

def conf_to_json(typ):
    file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "temp", "config.json5"
    )
    fil = open(file_path, "r")
    dic = json5.load(fil)
    return json5.dumps(dic[typ])
    
def update_json(typ, data):
    file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "temp", "config.json5"
    )
    fil = open(file_path, "r")
    dic = json5.load(fil)
    fil.close()
    pdata = json5.loads(data)
    fil = open(file_path, "w")
    dic[typ] = pdata
    json5.dump(dic, fil)
    fil.close()
