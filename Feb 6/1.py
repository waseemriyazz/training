# 1.Write a Python program to copy the contents of a file to another file

with open("Feb 6/1_file_1.txt", "r") as source:
    content = source.read()

with open("Feb 6/1_file_2.txt", "w") as dest:
    dest.write(content)