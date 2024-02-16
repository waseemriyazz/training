# Write a NumPy program to test if any of the elements of a given array is non-zero. Go to the editor
import numpy as np

arr = np.array([0, 0, 0, 4, 0])

if np.any(arr != 0):
    print("At least one element is non-zero.")
else:
    print("All elements are zero.")
