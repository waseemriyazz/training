# Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.
import numpy as np

arr1 = np.array([1.0, 2.0, 3.0])
arr2 = np.array([1.01, 1.99, 3.0])

equal = np.equal(arr1, arr2)
equal_within_tolerance = np.allclose(arr1, arr2, atol=0.02)

print("Equal:", equal)
print("Equal within tolerance:", equal_within_tolerance)
