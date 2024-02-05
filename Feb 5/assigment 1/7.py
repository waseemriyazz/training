# 7.Write a Python program to get the file size of a plain file
import os 

file_path = 'Feb 5/assigment 1/Questions.txt'


    # Get the file size
file_size = os.path.getsize(file_path)

    # Print the file size
print(f"File size of '{file_path}': {file_size} bytes")
