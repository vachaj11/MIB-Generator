Installation and usage
======================

Installation
------------

This is a Python project so you have to have a [Python interpreter](https://www.python.org/downloads/) installed on your machine. This project isn't yet packaged so
you will have to manually install the prerequisites which are Python libraries ``pyjson5`` and ``PySide6`` (optional, used only for the GUI). Install them using: ::

	$ pip install pyjson5 PySide6

Then either download the project manually or clone it to your desired location. No more installation steps should be needed.

Usage
-----

Navigate to the directory where you unpacked or cloned the project and run the program with: ::

	$ python3 main.py
	
If you're running the programm for the first time you should start by specifying the input/output files. This can be either done manually by modifying the file
``data/paths.json5`` or by running the script as: ::

	$ python3 main.py -p

There are a few more additional flags that the scripts accepts, to see all the options, run: ::

	$ python3 main.py --help
