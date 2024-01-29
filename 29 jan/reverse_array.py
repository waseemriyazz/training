size = int(input("Enter the number of elements "))
myList = []

for i in range(0, size):
    i = int(input())
    myList.append(i)
    
pos = int(input("Enter the position "))
j = size-1
for i in range(pos, size):
    if j>i:
        myList[i], myList[j] = myList[j], myList[i]
        j= j-1
    else:
        break
       
print(myList)