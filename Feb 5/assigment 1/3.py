# 3.Write a Python program to calculate the number of days between two date times.
import datetime
start_year = int(input("Enter start date's year : "))
start_month = int(input("Enter start date's month : "))
start_day = int(input("Enter start date's day : "))

end_year = int(input("Enter end date's year : "))
end_month = int(input("Enter end date's month : "))
end_day = int(input("Enter end date's day : "))

start_date = datetime.date(start_year, start_month, start_day)
end_date = datetime.date(end_year, end_month, end_day)

difference = ( end_date - start_date ).days

print(f"The differece between the two dates is {difference} days")