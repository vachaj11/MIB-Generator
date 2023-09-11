.. MIB Generator documentation master file, created by
   sphinx-quickstart on Thu Aug 24 12:20:36 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to MIB Generator's documentation!
=========================================

**MIB Generator** is a set of Python scripts that serve the puspose of generating MIB databases (Used in ESA's MCS SCOS 2000) from a set of header (and others) files written in C which define the structure of TM and TC packets. It is concieved mostly as a single script which the user runs from the terminal rather than a series of methods, but the structure of the project should hopefully allow easy modification of the generation process, which in the current implementation assumes one specific formatting of the inputted C-files (see :doc:`here <samples>` for more info).

.. note::
   This project is under active development.

.. toctree::
   :maxdepth: 1
   :caption: Documentation:

   About <about>
   Installation and building <installation>
   Usage <usage>
   Changing the code <change>
   C code examples <samples>

.. toctree::
   :maxdepth: 1
   :caption: Sub-packages
   
   Main sub-package <mib_generator.main>
   Parsing sub-package <mib_generator.parsing>
   Construction sub-package <mib_generator.construction>
   Generation sub-package <mib_generator.generation>
   Data sub-package <mib_generator.data>
   Temp sub-package <mib_generator.temp>
   Utilities sub-package <mib_generator.utilities>
   GUI sub-package <mib_generator.gui>

Indices
=======

* :ref:`genindex`
* :ref:`modindex`

