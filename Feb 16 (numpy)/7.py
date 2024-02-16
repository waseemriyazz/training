# Write a NumPy program to test element-wise for NaN of a given array. Go to the editor
import numpy as np

arr = np.array([1.0, np.nan, 3.0, np.inf])

print("NaN elements:", np.isnan(arr))
