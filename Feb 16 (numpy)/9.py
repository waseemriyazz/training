# Write a NumPy program to test if two arrays are element-wise equal within a tolerance.
import numpy as np

arr1 = np.array([1.0, 2.0, 3.0])
arr2 = np.array([1.01, 1.99, 3.0])

equal_within_tolerance = np.allclose(arr1, arr2, atol=0.02)

print("Arrays are equal within tolerance:", equal_within_tolerance)
