# 3.You are given an arbitrary array ‘arr’ consisting of N non-negative integers, where every element appears thrice except one. You need to find the element that appears only once.
# Sample Input 1:
# 4
# 1 2 1 1
# Sample Output 1:
# 2
size = int(input("Enter the number of elements (3n+1): "))
myList = []

# Input the elements into myList
for i in range(size):
    element = int(input("Enter element {}: ".format(i + 1)))
    myList.append(element)

# Count the occurrences of each element using a dictionary
myDict = {}
for num in myList:
    if num in myDict:
        myDict[num] += 1
    else:
        myDict[num] = 1

# Find the element that appears only once
for key, value in myDict.items():
    if value == 1:
        print("The element that appears only once is:", key)
        break
    