# 3.Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
import random
rands = []

for i in range(10):
    j = int(random.random()*100)
   
    rands.append(j)

with open("Feb 6/3_file_1.txt", "a")as file1:
    for num in rands:
        file1.write(str(num)+ "\n")

# reading the file
    
with open("Feb 6/3_file_1.txt", "r")as file2:
    nums = file2.readlines()
print("the nums are: ")
print(nums)

_sort = []
for num in nums:
    _sort.append(int(num.strip()))
_sort.sort()
with open("Feb 6/3_file_2.txt", "a")as file3:
    for num in _sort:
        file3.write(str(num)+ "\n")









        
