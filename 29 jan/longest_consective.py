size = int(input("Enter the size of array "))
myList = []

for i in range(0, size):
    i = int(input("Enter the {} element ".format(i+1)))
    myList.append(i)
myList.sort()
longest = 0 
curr = 0
key = myList[0]
for i in range(1, len(myList)):
    if  myList[i] - key == 1: 
        curr = curr + 1
        longest = max(curr, longest)
        key = myList[i]
    else :
        length = 0
    
print(longest+1)