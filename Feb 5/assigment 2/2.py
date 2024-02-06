# 2.Writing to CSV file

# writerows()
import csv

data = [['Name', 'Age'], ['John', '25'], ['Alice', '30']]

with open('Feb 5/assigment 2/2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    # writerow()
    # for row in data:
    #     writer.writerow(row)