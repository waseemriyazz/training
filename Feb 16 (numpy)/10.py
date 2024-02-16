# Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 1, 3])

print("Greater:", np.greater(arr1, arr2))
print("Greater or equal:", np.greater_equal(arr1, arr2))
print("Less:", np.less(arr1, arr2))
print("Less or equal:", np.less_equal(arr1, arr2))
