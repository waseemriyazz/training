# 3.Find Duplicates In Array
# Problem statement
# You are given an array/list 'ARR' consisting of N integers, which contains elements only in the range 0 to N - 1. Some of the elements may be repeated in 'ARR'. Your task is to find all such duplicate elements.

# Note:
# 1. All the elements are in the range 0 to N - 1.
# 2. The elements may not be in sorted order.
# 3. You can return the duplicate elements in any order.
# 4. If there are no duplicates present then return an empty array.

# Sample Input 1:
# 2
# 5
# 0 2 1 2 3 
# 7
# 3 2 1 3 2 1 5
# Sample Output 1:
# 2
# 1 2 3
# Explanation For Sample Input 1:
# For the first test case, since 2 is the only duplicate element, so we return it.

# For the second test case, since 1, 2, 3 are duplicates so we return them. Note that 2, 3, 1 and 3, 2, 1 are also acceptable.

size = int(input("Enter the size of array "))
myList = []

for i in range(0, size):
    i = int(input())
    myList.append(i)

ansList = []
flag = 0
index = 0 
myList.sort()
for i in range(0, len(myList)-1):
    if myList[i] == myList[i+1] and flag == 0 :
        ansList.append(myList[i])
        flag = 1
    if flag != 0 :
        if myList[i] == myList[i+1] and myList[index] != myList[i]:
            ansList.append(myList[i])
            index = index + 1 
           


print(ansList)