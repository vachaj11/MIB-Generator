I need to change...
===================
What entries are put in a MIB table which is associated to a...
	* TM packet -> Edit appropriate attribute of :obj:`mib_generator.construction.TM_packet.TM_packet`
	* TC command -> Edit appropriate attribute of :obj:`mib_generator.construction.TC_packet.TC_packet`
	* TC header -> Edit appropriate attribute of :obj:`mib_generator.construction.TC_packet.TC_header`
	* TM calibration -> Edit the corresponding class in :obj:`mib_generator.construction.calib`
	* TC decalibration/verification -> Edit the corresponding class in :obj:`mib_generator.construction.calib`
	
How a given file is parsed. This file has an ending...
	* ``.h`` -> Edit appropriate class/parsing method in :obj:`mib_generator.parsing.par_header`
	* ``.c`` -> Edit appropriate class/parsing method in :obj:`mib_generator.parsing.par_cfile`
	
Something about how the actual output MIB files are generated and checked...
	* -> Edit some method in :obj:`mib_generator.generation.gener`
	
Something about the general working of the script...
	* -> for general functioning of the script you want to change either :obj:`mib_generator.main.main.main` or
	  :obj:`mib_generator.parsing.load`
	* -> for the UI and GUI interface of the script you want to change either something in
	  general in :obj:`mib_generator.main.cli` or some module in :obj:`mib_generator.utilities`.
