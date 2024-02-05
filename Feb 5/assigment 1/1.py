# 1. Write a Python script to display the various Date Time formats -
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week

import datetime
a = datetime.datetime.now()
print("current date and time is : ", a)
print("current year is : ", a.year)
print("current year is : ", a.month)

d = datetime.date.today()
week_number = d.isocalendar()[1]
print("current week number is : ", week_number)

isoweekday = d.isoweekday()
print("current iso week day : ", isoweekday)
weekday = d.weekday()
print("current week number : ", weekday)
print( "current year day is : ", d.timetuple().tm_yday)
print("current day of month is : ", d.day)
print ("current day of week is : (iso){} or {}".format( isoweekday, weekday))


