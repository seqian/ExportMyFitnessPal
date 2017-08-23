#!/usr/bin/python
"""
Created on Tue Aug 22 00:16:12 2017

@author: Seqian Wang

Purpose: Employs python-myfitnesspal to export meal information into a CSV file. Automatically detect last time run from CSV, then import relevant data.
"""

# myfitnesspal store-password username
# Thanks for work @ https://github.com/coddingtonbear/python-myfitnesspal

import myfitnesspal, datetime, csv, os


# Will be reading from a username.login file, which is essentially a text file with the relevant info
client = myfitnesspal.Client('seqian@outlook.com')

# Function to calculate date range. From somewhere on StackOverflow
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

# Setting Days
first_day = datetime.date(2017, 8, 11)
# Would come from csv file
# Until then...
latest_backup = first_day
today = datetime.date.today()

with open('dict.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for date in daterange(latest_backup, today):
        day = client.get_date(date)
        for meal_index in range(len(day.keys())):
            meal_time = day.keys()[meal_index]
            for ingredient in range(len(day.meals[meal_index].entries)):
                row = [day, date.strftime('%A'), meal_index, meal_time]
                row.append(day.meals[meal_index].entries[ingredient])
                writer.writerow(row)
