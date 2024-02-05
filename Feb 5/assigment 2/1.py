# 1.Reading from CSV file
import csv

with open('Feb 5/assigment 2/scores.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
