# 11.Write a Python program to read a given CSV file having tab delimiter.
import csv

# Specify the path to the CSV file with tab delimiter
csv_file_path = input("Enter the path to the CSV file with tab delimiter: ")

try:
    # Open the CSV file in read mode
    with open(csv_file_path, 'r', newline='') as csv_file:
        # Create a CSV reader with tab delimiter
        csv_reader = csv.reader(csv_file, delimiter='\t')

        # Read and print each row as a list of strings
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print(f"Error: File not found at {csv_file_path}")
except Exception as e:
    print(f"Error: {e}")