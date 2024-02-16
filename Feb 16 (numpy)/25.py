# Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
import numpy as np

# Create a 3x4 matrix with values from 10 to 21
matrix = np.arange(10, 22).reshape(3, 4)

print("3x4 Matrix filled with values from 10 to 21:\n", matrix)
