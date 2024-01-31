size = int(input("Enter the value of N : "))
myMatrix = []
for i in range(0, size):
    element = []
    for j in range(0, size):

        k=int(input("Enter the value of element {} {} ".format(i, j)))
        element.append(k)
    myMatrix.append(element)
total_sum = 0
for i in range(size):
    for j in range(size):
        if i == j or j == 0 or i == 0 or i == size - 1 or j == size - 1 or i + j == size - 1:
            total_sum = total_sum + myMatrix[i][j]
print(total_sum)