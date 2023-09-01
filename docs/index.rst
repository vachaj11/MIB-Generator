.. MIB Generator documentation master file, created by
   sphinx-quickstart on Thu Aug 24 12:20:36 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to MIB Generator's documentation!
=========================================

**MIB Generator** is a set of Python scripts that serve the puspose of generating MIB databases (Used in ESA's MCS SCOS 2000) from a given set of packet header (and others) files written in C. It is concieved mostly as a single script which the user runs from ``main.py`` rather than a series of methods, but the structure of the project should hopefully allow easy modification of the generation process, which itself in the current implementation heavily assumes one specific structure of the inputted C-files.

.. note::
   This project is under active development.

.. toctree::
   :maxdepth: 1
   :caption: Documentation:

   About <about>
   Installation and usage <usage>
   Changing the code <change>

.. toctree::
   :maxdepth: 1
   :caption: Sub-packages
   
   Main sub-package <mib_generator.main>
   Parsing sub-package <mib_generator.parsing>
   Construction sub-package <mib_generator.construction>
   Generation sub-package <mib_generator.generation>
   Data sub-package <mib_generator.data>
   Utilities sub-package <mib_generator.utilities>

Indices
=======

* :ref:`genindex`
* :ref:`modindex`

