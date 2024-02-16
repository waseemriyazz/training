# Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.
import numpy as np

vector = np.arange(21)

vector[9:16] *= -1

print("Modified vector:", vector)
