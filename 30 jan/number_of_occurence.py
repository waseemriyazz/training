# 1.Number of occurrence
# Problem statement
# You have been given a sorted array/list of integers 'arr' of size 'n' and an integer 'x'.
# Find the total number of occurrences of 'x' in the array/list.
# Example:
# Input: 'n' = 7, 'x' = 3
# 'arr' = [1, 1, 1, 2, 2, 3, 3]
# Output: 2
# Explanation: Total occurrences of '3' in the array 'arr' is 2.


size = int(input("Enter the size of array "))
myList = []

for i in range(0, size):
    i = int(input())
    myList.append(i)

myList.sort()

key = int(input("Enter the number to be found "))
count = 0 
for i in myList:
    if i == key :
        count = count+1
print("{} occurs {} times".format(key, count))