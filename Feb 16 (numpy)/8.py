# Write a NumPy program to test element-wise for complex number, real number of a given array. Also test if a given number is a scalar type or not.
import numpy as np

arr = np.array([1, 2.5, 3 + 2j])

print("Complex elements:", np.iscomplex(arr))
print("Real elements:", np.isreal(arr))
print("Scalar type check:", np.isscalar(2.5))
