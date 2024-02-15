import numpy as np

size1 = int(input("Enter size of first array: "))
size2 = int(input("Enter size of second array: "))
arr1, arr2 = [],[]
for i in range (size1):
    temp = int(input(f"Enter element {i+1} of first array : " ))
    arr1.append(temp)
for i in range (size2):
    temp = int(input(f"Enter element {i+1} of second array : " ))
    arr2.append(temp)



# Create sample arrays
array1 = np.array(arr1)
array2 = np.array(arr2)

# Use np.in1d to check if each element of array1 is present in array2
is_present = np.in1d(array1, array2)

# Print the results
print("Array1:", array1)
print("Array2:", array2)
print("Compare each element of array1 and array2:")
print(is_present)
