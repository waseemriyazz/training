# Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number).
import numpy as np

arr = np.array([1.0, np.inf, np.nan, 5.0])

print("Finite elements:", np.isfinite(arr))
