# 4.Appending To a File in Python
# i- Append-adds at last

with open('Feb 5/assigment 2/4.txt', 'a') as file:
    file.write("Appended text\n")

# ii - Write
with open('Feb 5/assigment 2/4.txt', 'w') as file:
    file.write("Overwritten text\n")