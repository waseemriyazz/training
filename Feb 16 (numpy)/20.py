# Write a NumPy program to create a 3X4 array using and iterate over it.
import numpy as np

array_3x4 = np.arange(12).reshape(3, 4)

print("Array 3x4:\n", array_3x4)

for row in array_3x4:
    for element in row:
        print(element, end=" ")
    print()
