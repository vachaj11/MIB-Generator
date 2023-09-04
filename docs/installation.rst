Installation and building
=========================

This is a Python project so in any case you have to have a `Python interpreter <https://www.python.org/downloads/>`_ installed on your machine. 

Installation
------------

The releases are published to `PyPI <https://pypi.org/project/mib-generator>`_ and so the project can be most easily installed with: ::

	$ pip install mib-generator
	
Or alternatively: ::

	$ python3 -m pip install mib-generator
	

Building from source
--------------------

In case you want to build the project from source yourself:

Clone the source repository using: ::

	$ git clone https://github.com/vachaj11/MIB-Generator.git
	
Navigate to the cloned directory: ::

	$ cd MIB-Generator

The building process requires the Python ``build`` package. Install it (or check the installation) with: ::

	$ python3 -m pip install --upgrade build

Build the MIB Generator package with: ::

	$ python3 -m build

If this finishes successfully, navigate to the build directory: ::

	$ cd dist
	
And install the built package with: ::

	$ python3 -m pip install *.whl
	
(Replace the ``*.whl`` with the full name in case you have multiple versions built.)

Running without building
------------------------

The set of scripts can also be used directly without any building and packet installation. In such case, clone the source code into desired directory with: ::

	$ git clone https://github.com/vachaj11/MIB-Generator.git

Before running the cloned code, you will have to manually install the prerequisite python libraries, which are ``json5`` and ``PySide6`` (optional, used only for the GUI). Install them using (assuming a standard Python3 environment): ::

	$ python3 -m pip install json5 PySide6

You should then be able to directly run any script found in the package, subpackages and modules in the ``./src`` directory.
