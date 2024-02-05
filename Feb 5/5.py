# 5.Write a Python program to read first n lines of a file.
number_of_lines = int (input("Enter the number of lines to be read : "))
text_file = open('Feb 5/Questions.txt', 'r')
content = text_file.readlines()[:number_of_lines]

print(content)