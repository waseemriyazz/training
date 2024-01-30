# 2.Find First and Last Position of Element in Sorted Array
# Problem statement
# You are given a non-decreasing array 'arr' consisting of 'n' integers and an integer 'x'. You need to find the first and last position of 'x' in the array.
# Note:
# 1. The array follows 0-based indexing, so you need to return 0-based indices.
# 2. If 'x' is not present in the array, return {-1 -1}.
# 3. If 'x' is only present once in the array, the first and last position of its occurrence will be the same.
# Example:
# Input:  arr = [1, 2, 4, 4, 5],  x = 4
# Output: 2 3
# Explanation: The given array’s 0-based indexing is as follows:
#  1      2     4     4     5
#  ↓      ↓     ↓     ↓     ↓
#  0      1     2     3     4
# So, the first occurrence of 4 is at index 2, and the last occurrence of 4 is at index 3.

size = int(input("Enter the size of array "))
myList = []

for i in range(0, size):
    i = int(input())
    myList.append(i)

key = int(input("Enter the number to be found "))

myList.sort()

start , end  = -1 , -1 

for i in range(0 , len(myList)):
    if key == myList[i] and start == -1:
        start = i
        
    if key == myList[i]:
        end = i
    
print(start, end )

