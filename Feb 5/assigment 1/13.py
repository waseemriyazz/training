# 13.Write a Python program to read specific columns of a given CSV file and print the content of the columns.
import csv

# Specify the path to the CSV file
csv_file_path = "Feb 5/assigment 1/scores.csv"

# Specify the column indices to read
column_indices = input("Enter the column indices (comma-separated): ")
column_indices = [int(index) for index in column_indices.split(',')]

try:
    # Open the CSV file in read mode
    with open(csv_file_path, 'r', newline='') as csv_file:
        # Create a CSV reader
        csv_reader = csv.reader(csv_file)

        # Read and print specific columns
        for row in csv_reader:
            selected_columns = [row[index] for index in column_indices]
            print(selected_columns)
except FileNotFoundError:
    print(f"Error: File not found at {csv_file_path}")
except Exception as e:
    print(f"Error: {e}")
