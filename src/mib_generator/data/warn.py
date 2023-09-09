"""Takes care of warning and errors that can be raised by the rest of the program.

This module holds both definition of all the errors and warnings that can occur throughout and a method that can be used to 
raise them. (This is made this centralised so that the raising method can be easily changed later if e.g. the UI changes.)

Attributes:
    warnings (dict): A dictionary containing the text definitions of all the possible warnings.
    errors (dict): A dictionary containing the text definitions of all the possible errors.
    display (None or some object): Defines (or holds the object) where the warnings should be raise.
"""

warnings = {
    "WCC1": "Wasn't able to find matching calibration for {} in packet {}.",
    "WCC2": "Wasn't able to find matching decalibration for {} in command {}.",
    "WCC3": "Wasn't able to find the required verification {} for command {}.",
    "WCT1": "Wasn't able to find the common Tc header.",
    "WCT2": "Wasn't able to find the common Tm header.",
    "WCM1": "Wasn't able to find the numerical value of {}.",
    "WCM2": "Wasn't able to establish the link of packet {} to any header structure.",
    "WGM1": "Found repedition in table {}. Deleting rows: {}{}",
    "WGM2": "Tm-packets {} and {} share packet type, subtype and apid, but differ in specification of additional identification field.",
    "WGM3": "Tm-packets {} and {} share packet type, subtype and apid, but do not have additional identification field specified.",
    "WGM4": "The value in table {}, column {}, row {} doesn't have the required type.{}",
    "WGM5": "Missing a mandatory entry in table {}, column {}, row {}.",
    "WGG1": "Didn't get an input object on basis of which the table {} could be constructed.",
    "WGG2": "The construction of the table {} isn't yet implemented. And hence it wasn't generated.",
    "WMM1": "PySide6 not found. Please install it in order to show the parsed files",
    "WPL1": "Failed to construct the list of available enumerations.",
    "WPM1": "Invalid logic encountered when parsing preprocessor directives.",
    "WTT1": "The path {} for file {} does not exist, consider using previous value {}.",
    "WTT2": "The path {} for file {} does not exist (and there is no valid previous value to use in its place).",
    "WUU1": "The directory {} to which the config files are to be saved doesn't exist."
}

errors = {
    "EPL1": "Failed to load (some of) the input/output paths.",
    "EPL2": "Failed to load the {} C file.",
    "EPM1": "Falied loading json5 comment: {}",
}

display = None

def disp_update(var):
    """Update the :attr:`display` global variable in this module to the specified value.
    
    This quite ugly method (or approach) serves the purpose of specifying to the method that takes care of raising warnings, that
    the warnings shouldn't be printed to terminal but rather added to the object's text (the passed object is expected to be some GUI console).
    
    Args:
        var (object such as PySide6.QtWidgets.QTextEdit): The object to be assigned to the :attr:`display` global variable.
    """
    globals()["display"] = var

def raises(ID, *data):
    """Raise warning/error with the given ID.

    This method looks up a warning/error text for a given passed ID, formats it with other passed parameters and
    then displays it - either to terminal if the global attribute :attr:`display` is ``None`` or to the object that this attribute holds..

    Args:
        ID (str): The ID identifying the warning/error of format 3 capital letters + one-digit number.
        \*data (\*args): Additional parameters which are to be formatted into the warning/error text.
    """
    if ID[:1] in {"w", "W"}:
        if ID in warnings.keys():
            stri = "Warn.:\t" + warnings[ID].format(*data)
        else:
            stri = "Warn.:\tUnspecified warning with ID {} encountered.".format(ID)
    elif ID[:1] in {"e", "E"}:
        if ID in errors.keys():
            stri = "Error:\t" + errors[ID].format(*data)
        else:
            stri = "Error:\tUnspecified error with ID {} encountered.".format(ID)
    if not display:
        print(stri)
    else:
        display.append(stri)
