# Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.
import numpy as np

vector = np.arange(15, 56)

print("Vector:", vector)
print("Values excluding the first and last:", vector[1:-1])

