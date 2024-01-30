size1 = int(input("Enter the number of digits in 1st number "))
myList1 = []

for i in range(0, size1):
    i = int(input())
    myList1.append(i)

size2 = int(input("Enter the number of digits in 2nd number "))
myList2 = []

for i in range(0, size2):
    i = int(input())
    myList2.append(i)

num1 = 0
num2 = 0 
for i in range(size1-1, -1, -1):
    num1 = num1*10 + myList1[i]
for i in range(size2-1, -1 ,-1):
    num2 = num2*10 + myList2[i]
print(num1 + num2)