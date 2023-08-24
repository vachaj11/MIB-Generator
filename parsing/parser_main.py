"""This module is a starting point for parsing of C-files and holds class which plays the role of their interpretation."""
import parsing.par_header as parh
import parsing.par_cfile as parc
import parsing.par_methods as parm


class file:
    """
    class resresenting the file being analysed, its structure, etc...
    
    Parameters:
        stri: string
            a string of the file text to be parsed
        header: boolean
            parameter denoting whether file is a header or normal C file
    """

    def __init__(self, stri, header):
        self.text = stri
        self.max_position = len(stri)
        self.lines = parm.line_index(stri)
        self.text_o, self.text_c = parm.split_comment(stri)
        self.text_f = parm.preproc_filter(self.text_o)
        if header:
            self.structures = parh.str_parse(self.text_f)
        else:
            self.structures = parc.str_parse(self.text_f)
        self.comments = parm.com_parse(self.text_c)
        self.link = self.linker()

    def linker(self):
        """
        Link each comment to a corresponding C-object in the file
        
        Returns:
            pairs: list
                pairs of comments and their corresponding objects
        """
        pairs = []
        for i in self.comments:
            ind = i.start
            elem = {}
            minim = 50000
            for l in self.structures:
                if l.start <= ind <= l.end:
                    if l.type != "enum":  # very ugly bodge again
                        for k in l.elements:
                            if ind - k.start >= 0 and ind - k.start <= minim:
                                elem = k
                                minim = ind - k.start
                    else:
                        elem = l
                        minim = 49999

                    break
            if minim == 50000:
                for l in self.structures:
                    if l.start - ind >= 0 and l.start - ind <= minim:
                        elem = l
                        minim = l.start - ind
            pairs.append([i, elem])
            elem.comment.append(i)
            i.structure = elem
        return pairs


def main(name="/home/vachaj11/Documents/MIB/start/src/PUS_TmDefs.h"):
    """
    Created a parsed Python representation from the given file.
    
    Parameters: 
        name: string
            Path to the file 
    """
    try:
        fil = open(name, "r")
        c = fil.read()
        fil.close()
    except:
        c = ""
    if name[-1] == "h":
        x = file(c, True)
    else:
        x = file(c, False)
    x.path = name
    return x
