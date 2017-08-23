# ExportMyFitnessPal

Employs python-myfitnesspal from coddingtonbear to export MyFitnessPal data to CSV file
Pretty straightforward, run once a week to export and append
https://github.com/coddingtonbear/python-myfitnesspal

On Windows, requires curses, for which binary files can be found at http://www.lfd.uci.edu/~gohlke/pythonlibs/#curses

Thanks to https://stackoverflow.com/questions/35850362/importerror-no-module-named-curses-when-trying-to-import-blessings

## Installation

To install
	pip install myfitnesspal
	pip install curses-2.2-cp36-cp36m-win_amd64

To store your MyFitnessPal password in the system keyring, run:
	myfitnesspal store-password my_username

Note to future self:
1. Remove email address from online repository

Done
2. Add to exclusion files email address, + csv files