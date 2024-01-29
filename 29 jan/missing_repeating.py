# 3.You are given an array of size ‘N’. The elements of the array are in the range from 1 to ‘N’.
# Ideally, the array should contain elements from 1 to ‘N’. But due to some miscalculations, there is a number R in the range [1, N] which appears in the array twice and another number M in the range [1, N] which is missing from the array.
# Your task is to find the missing number (M) and the repeating number (R).
# For example:
# Consider an array of size six. The elements of the array are { 6, 4, 3, 5, 5, 1 }. 
# The array should contain elements from one to six. Here, 2 is not present and 5 is occurring twice. Thus, 2 is the missing number (M) and 5 is the repeating number (R). 
# Follow Up
# Can you do this in linear time and constant additional space? 

size = int(input("Enter the size of array "))
myList = []

for i in range(0, size):
    i = int(input())
    myList.append(i)
#sort the array first
myList.sort()
#iterate through the list to find a  number where the differece between current and next is 0
repeating = 0
for i in range(0, len(myList)-1):
    if myList[i+1] - myList[i] == 0:
        repeating = myList[i]
expected_sum = (len(myList)*(len(myList)+1))//2
actual_sum = 0
for i in myList:
    actual_sum = actual_sum + i
missing = expected_sum - actual_sum + repeating
print("missing", missing)
print("repeating", repeating)

