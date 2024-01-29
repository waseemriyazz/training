size = int(input("Enter the size of array "))
myList = []

for i in range(0, size):
    i = int(input())
    myList.append(i)
key = int(input("Enter the sum of triplet"))
for i in myList:
    for j in range (1, len(myList)):
        for k in range (2, len(myList)):
            if j != k and k != i and i + myList[j] + myList[k] == key:
                print(i , myList[j] , myList[k])
