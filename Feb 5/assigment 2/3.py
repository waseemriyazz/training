# 3.print the min, max and avg score of given score.csv file
import csv

scores = []

with open('Feb 5/assigment 2/scores.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        scores.append(int(row[1]))

print("Min Score:", min(scores))
print("Max Score:", max(scores))
print("Avg Score:", sum(scores) / len(scores))