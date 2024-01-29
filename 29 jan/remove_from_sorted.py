size = int(input("Enter the size of array "))
myList = []

for i in range(0, size):
    i = int(input())
    myList.append(i)
myList.sort()
myset = set()
for i in myList:
    myset.add(i)
print(len(myset))