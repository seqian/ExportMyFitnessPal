#!/usr/bin/python
"""
Created on Tue Aug 22 00:16:12 2017

@author: Seqian Wang

Purpose: Employs python-myfitnesspal to export meal information into a CSV file. Automatically detect last time run from CSV, then import relevant data.
"""

# myfitnesspal store-password username
# Thanks for work @ https://github.com/coddingtonbear/python-myfitnesspal

import myfitnesspal
import datetime

# Look into http://www.tutorialspoint.com/python/python_date_time.htm for properly using date and time in Python

# Will be reading from a username.login file, which is essentially a text file with the relevant info
client = myfitnesspal.Client('seqian@outlook.com')

firstDate = '2017-08-11'
# Would come from csv file
# lastBackup
today = datetime.datetime.today()

meals = client.get_date(2017, 8, 11)

for i in range(day, 21myfmy):
	meals = client.get_date(year, month, 2)
    
# Write to CSV file