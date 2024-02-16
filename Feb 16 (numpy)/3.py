# Write a NumPy program to test whether none of the elements of a given array is zero.
import numpy as np

arr = np.array([1, 2, 3, 4, 0])

if np.all(arr != 0):
    print("None of the elements are zero.")
else:
    print("There are zero elements.")
