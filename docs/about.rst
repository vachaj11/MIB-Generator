About the script
================
The workings of the MIB generator can be divided into multiple steps:

	1. Interaction with the user and configuration. These matters are handled by the initial Python script in 
	   the :obj:`mib_generator.main` package and various utilities in the :obj:`mib_generator.utilities` package.
	2. Parsing of the C-file into a format which is easily manipulated in Python. This is mainly the job of the
	   :obj:`mib_generator.parsing` package.
	3. Construction of Python objects which represent TM packets, TC commands, various calibrations, etc. from the
	   parsed representations of C-files. This is done by modules in the :obj:`mib_generator.construction` package.
	4. Generation of MIB tables, their checking and saving to appropriate location. This is done by
	   the :obj:`mib_generator.generation` package.
	   
For a further general understanding of how this code functions, I recommend you to start by reading the documentation for the
:obj:`mib_generator.main.main` module and then continue from there on.

Currently, four C files are expected as a basis for the generation process:

	1. Tm ``.h`` file. This should include information about the structure of Tm packets, their entries, associated calibrations, etc.
	2. Tm ``.c`` file. This should include mainly list of all Tm packet types and some of their meta-characteristics.
	3. Tc ``.h`` file. This should include information about the structure of Tc commands, their entries, headers of Tc packets and
	   associated decalibrations and verifications.
   	4. TcTm ``.h`` file. This should include information common to both Tm and Tc packets like the common id structures or various enums. 
	
For the expected content of these files in more detail see :doc:`code examples here<samples>`. 
