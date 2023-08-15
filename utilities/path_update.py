"""This module allows for automatic updates to the file paths specified in paths.json5"""
import json5
import os


def update():
    """Run a series of queries asking user to specify valid paths to input files."""
    file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "data", "paths.json5"
    )
    fil = open(file_path, "r")
    leg_data = json5.load(fil)
    fil.close()
    data = {}
    valid_TmH = False
    print("The current absolute path is: " + os.getcwd())
    print("------")
    while not valid_TmH:
        print("State relative or absolute path to Tm Header file.")
        print("Currently this path is: " + str(leg_data["TmHeader"]))
        print("(press Enter if you want to keep this value)")
        path = input("Path: ")
        if path == "" and os.path.isfile(leg_data["TmHeader"]):
            data["TmHeader"] = leg_data["TmHeader"]
            valid_TmH = True
        elif os.path.isfile(path):
            data["TmHeader"] = os.path.abspath(path)
            valid_TmH = True
        else:
            print("Error:\tFailed to find the specified file, try again.")
        print("------")
    valid_TcTmH = False
    while not valid_TcTmH:
        print("State relative or absolute path to TcTm Header file.")
        print("Currently this path is: " + str(leg_data["TcTmHeader"]))
        print("(press Enter if you want to keep this value)")
        path = input("Path: ")
        if path == "" and os.path.isfile(leg_data["TcTmHeader"]):
            data["TcTmHeader"] = leg_data["TcTmHeader"]
            valid_TcTmH = True
        elif os.path.isfile(path):
            data["TcTmHeader"] = os.path.abspath(path)
            valid_TcTmH = True
        else:
            print("Error:\tFailed to find the specified file, try again.")
        print("------")
    valid_TmC = False
    while not valid_TmC:
        print("State relative or absolute path to Tm C file.")
        print("Currently this path is: " + str(leg_data["TmFile"]))
        print("(press Enter if you want to keep this value)")
        path = input("Path: ")
        if path == "" and os.path.isfile(leg_data["TmFile"]):
            data["TmFile"] = leg_data["TmFile"]
            valid_TmC = True
        elif os.path.isfile(path):
            data["TmFile"] = os.path.abspath(path)
            valid_TmC = True
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
    fil = open(file_path, "w")
    fil.write("// This file stores various paths to source/output files\n")
    fil.write(json5.dumps(data))
    fil.close()
