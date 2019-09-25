"""
Project Euler Problem 19
========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""
from collections import OrderedDict

daysPerMonth = OrderedDict([("January", 31), ("February", 28), ("March", 31),
                            ("April", 30), ("May", 31), ("June", 30),
                            ("July", 31), ("August", 31), ("September", 30),
                            ("October", 31), ("November", 30), ("December", 31)])

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def isLeap(year):
    # See https://en.wikipedia.org/wiki/Leap_year#Algorithm
    if year % 4 != 0:
        leap = False
    elif year % 100 != 0:
        leap = True
    elif year % 400 != 0:
        leap = True
    else:
        leap = True
    return leap


day = 1  # 1 Jan 1901 is Tuesday
sundays = 0
for year in range(1901, 2001):
    for month in daysPerMonth:
        # Get weekday for day
        weekday = weekdays[day]
        # Check if it's sunday
        if weekday == "Sunday":
            sundays += 1
        # Increase day by month length
        day += daysPerMonth[month]
        # Handle leap year
        if isLeap(year) and month == "February":
            day += 1
        # Modulo day by week length
        day = day % 7


print(sundays)
