# 12.Write a Python program that reads a CSV file and remove initial spaces, quotes around each entry and the delimiter.
import csv

# Specify the path to the CSV file
csv_file_path = "Feb 5/assigment 1/test3.csv"

try:
    # Open the CSV file in read mode
    with open(csv_file_path, 'r', newline='') as csv_file:
        # Create a CSV reader
        csv_reader = csv.reader(csv_file)

        # Read and process each row
        for row in csv_reader:
            # Remove initial spaces, quotes, and delimiter from each entry
            cleaned_row = [entry.strip().strip('"') for entry in row]

            # Print the cleaned row
            print(cleaned_row)
except FileNotFoundError:
    print(f"Error: File not found at {csv_file_path}")
except Exception as e:
    print(f"Error: {e}")
