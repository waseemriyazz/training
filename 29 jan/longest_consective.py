size = int(input("Enter the size of array "))
myList = []

for i in range(0, size):
    i = int(input("Enter the {} element ".format(i+1)))
    myList.append(i)
myList.sort()
