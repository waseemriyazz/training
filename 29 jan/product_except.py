size = int(input("Enter the size of array "))
myList = []

for i in range(0, size):
    i = int(input())
    myList.append(i)

product = 1 
for i in myList:
    product = product * i
finalList = []
for i in range(0, size):
    finalList.append(product // myList[i])
print(finalList)