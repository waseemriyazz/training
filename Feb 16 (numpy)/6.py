# Write a NumPy program to test element-wise for positive or negative infinity.
import numpy as np

arr = np.array([1.0, np.inf, -np.inf, 5.0])

print("Positive infinity:", np.isposinf(arr))
print("Negative infinity:", np.isneginf(arr))

