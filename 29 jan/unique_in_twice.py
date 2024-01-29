# size has to be odd 
# only one number should be unique
size = int(input("Enter the number of elements "))
myList = []

for i in range(0, size):
    i = int(input())
    myList.append(i)
answer = 0 
for i in myList:
    answer = answer ^ i
print(answer)