size1 = int(input("Enter the number of elements in array "))
k = int(input("Enter the value of k "))
myList1 = []
ans = []


for i in range(0, size1):
    i = int(input())
    myList1.append(i)

myList1.sort
mySet = set()
for i in myList1:
    mySet.add(i)

for i in mySet:
    ans.append(i)

for i in range ( len(ans)-1, len(ans)-k-1, -1):
    print(ans[i])


