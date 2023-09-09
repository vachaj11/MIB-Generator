Usage
=====

Finding and running the main script:

With the package installed
--------------------------

If you have the project installed as a package (either from `PyPI <https://pypi.org/project/mib-generator>`_ or built yourself.), running is should be as easy as typing: ::

	$ mib-gen
	
or in case of a more general installation: ::

	$ python3 -m mib-gen
	
if even this doesn't work than you can also run directly the Python file  ``mib-gen`` found in the ``.../bin`` folder of your Python installation.

Running without building
------------------------

Navigate to the directory where you unpacked or cloned the project and run the program with: ::

	$ python3 src/main/cli.py

This does the same as running ``$ mib-gen`` would with the project installed as a package.

First time
----------

If you're running the program for the first time, you should start by specifying the input/output files. This can be either done manually by modifying the file
``data/paths.json5`` (found in ``.../src//data/`` with respect to the rest of the package) or by running the script as: ::

	$ mib-gen -p

Flags and options
-----------------

The CLI of the main script also accepts a few additional flags, to see all of the options and their consequences, run: ::

	$ mib-gen --help

GUI
---

A simple GUI is provided for the program. Run it with: ::

	$ mib-gen-gui

more generatlly: ::

	$ python3 -m mib-gen-gui

or without installation: ::

	$ python3 src/mib_generator/gui/mainwindow.py
