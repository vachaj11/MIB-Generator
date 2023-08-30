About the script
================
The workings of the MIB generator can be divided into multiple steps:

	1. Interaction with the user and configuration. These matters are handled by the initial Python script in 
	   the :obj:`main` module and various utilities in the :obj:`utilities` package.
	2. Parsing of the C-file into a format which is easily manipulated in Python. This is mainly the job of the
	   :obj:`parsing` package.
	3. Construction of Python objects which represent TM packets, TC commands, various calibrations, etc. from the
	   parsed representations of C-files. This is done by modules in the :obj:`construction` package.
	4. Generation of MIB tables, their checking and saving to appropriate location. This is done by the :obj:`generation`
	   package.
	   
For a further general understanding of how this code functions, I recommend you to start by reading the documentation for the
:obj:`main` module and then continue from there on.
