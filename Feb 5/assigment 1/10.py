# 10.Write a Python program to read each row from a given csv file and print a list of strings.
import csv
csv_file_path = "Feb 5/assigment 1/test.csv"

try:
    # Open the CSV file in read mode
    with open(csv_file_path, 'r') as csv_file:
        # Create a CSV reader
        csv_reader = csv.reader(csv_file)

        # Read and print each row as a list of strings
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print(f"Error: File not found at {csv_file_path}")
except Exception as e:
    print(f"Error: {e}")