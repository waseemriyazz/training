# 8.Write a Python program that takes a text file as input and returns the number of words of a given text file.
# # Note: Some words can be separated by a comma with no space.
text_file = open('Feb 5/Questions.txt', 'r')
content = text_file.read()
content = content.replace(",", " ")
words = content.split()
print(f"The number of words present in the file are {len(words)}")

