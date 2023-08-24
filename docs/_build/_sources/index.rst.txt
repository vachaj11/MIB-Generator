.. MIB Generator documentation master file, created by
   sphinx-quickstart on Thu Aug 24 12:20:36 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to MIB Generator's documentation!
=========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


MIB Generator documentation
========
**MIB Generator** is a set of python scripts that serve the puspose of generating MIB databases (Used in ESA's MCS SCOS 2000) from a given set of packet header files written in C. It is concieved mostly as a single script which the user runs from *main.py* rather than a series of methods, but the structure of the project should hopefully allow easy modification of the generation process, which itself in the current implementation heavily assumes one specific structure of the inputted C-files.
.. note::
   This project is under active development.
