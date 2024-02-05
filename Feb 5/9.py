# 9.Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
for char in range(ord('A'), ord('Z') + 1):
    file_name = chr(char) + ".txt"
    with open(file_name, 'w') as file:
        # Write some content to each file (optional)
        file.write(f"Content of {file_name}\n")
    print(f"File '{file_name}' created.")
    