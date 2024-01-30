size = int(input("Enter the size of array "))
myList = []

for i in range(0, size):
    i = int(input("Enter the {} element ".format(i+1)))
    myList.append(i)

right = int(input("Enter the value of right "))
left = int(input("Enter the value of left "))
sumr = 0
suml = 0
for i in range(0, right):
    sumr = sumr + myList[ i % len(myList) ]
for i in range(0, left):
    suml= suml + myList[i % len(myList) ]
    
print(sumr-suml)
