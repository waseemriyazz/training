# 2.Write a Python program to combine each line from first file with the corresponding line in second file.
with open("Feb 6/2_file_1.txt", "r") as source1:
    content1 = source1.readlines()

print(f"The following list consist of all the lines of file 1 \n {content1}")
with open("Feb 6/2_file_2.txt", "r") as source1:
    content2 = source1.readlines()

print(f"The following list consist of all the lines of file 2 \n {content2}")

content3 = []
for line1, line2 in zip(content1, content2):

    newline = line1.strip() + " " + line2.strip()
    newline = newline + "\n"
    content3.append(newline)
print(f"The following list consist of all the lines to be put in file 3 \n {content3}")

with open("Feb 6/2_file_3.txt", "w") as dest:
     dest.writelines(content3)

