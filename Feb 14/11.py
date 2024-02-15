# Importing the NumPy library
import numpy as np

# Creating an array of integers
nums = np.array([70, 50, 20, 30, -11, 60, 50, 40])

# Displaying the original array
print("Original array:")
print(nums)

# Partitioning the array at the 4th position
print("\nAfter partitioning on 4 the position:")
print(np.partition(nums, 4)) 
