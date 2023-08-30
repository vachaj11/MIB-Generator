# MIB Generator
[![Docs](https://img.shields.io/badge/docs-2023_08_30-green)](docs/_build/index.html)
[![Black](https://img.shields.io/badge/code_style-black-black)](https://github.com/psf/black)

A set of python scripts that create a MIB database from inputted C-header files.
Prerequisite python libraries are `pyjson5` and `PySide6` (optional). Install them using (assuming a standard Python3 environment):
```
pip install pyjson5 PySide6
``` 
To run the scripts, specify the relevant input/output paths in "data/paths.json5"  (or run with flag `-p`) and run:
```
python3 main.py
```
(run with flag `-h` to show all available options)
