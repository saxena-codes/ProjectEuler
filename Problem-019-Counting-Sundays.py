"""
Problem 19 - Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
    April, June and November.
- All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
from datetime import datetime, timedelta

def find_first_sunday(year, month):
    d = datetime(year, int(month), 7)
    offset = -d.weekday() - 1 #weekday = 0 means monday
    d = d + timedelta(offset)
    d = str(d)
    d = d.split()
    return d[0]

answer = 0
# Looping through year 
year = 1901
while year <= 2000:

    # Looping through month
    month = 1
    while month <= 12:
        first_sunday = find_first_sunday(year, month)

        # A simple hack to ensure the comparing date matches
        comparing_date = ""
        if month%10 == 0 or month%11 == 0 or month%12 == 0:
            comparing_date = f"{year}-{month}-01"
        else:
            comparing_date = f"{year}-0{month}-01"

        if first_sunday == comparing_date:
            answer += 1

        month += 1
    year += 1

print("Answer:")
print(answer)