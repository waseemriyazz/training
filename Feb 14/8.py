import numpy as np

def round_and_abs(array):
 """
 Rounds elements of an array to the nearest integer and calculates absolute values element-wise.

 Args:
   array: A NumPy array.

 Returns:
   A NumPy array with rounded and absolute values.
 """

 # Round elements to nearest integer using np.round
 rounded_array = np.round(array)

 # Calculate absolute values using np.abs
 abs_values = np.abs(rounded_array)

 return abs_values

# Sample array
array = np.array([-0.7, -1.5, -1.7, 0.3, 1.5, 1.8, 2.0])

# Print the original array
print("Original array:")
print(array)

# Round and calculate absolute values
rounded_abs_array = round_and_abs(array)

# Print the rounded and absolute values
print("\nRounded elements of the array to the nearest integer:")
print(rounded_abs_array)
