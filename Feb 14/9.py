import numpy as np

def calculate_differences(array):
  """
  Calculates the difference between neighboring elements, element-wise,
  and prepends [0, 0] and appends [200] to the array.

  Args:
    array: A NumPy array.

  Returns:
    A new NumPy array with the calculated differences, prepended and appended values.
  """

  
  differences = np.diff(array)
  prepend_array = np.array([0, 0])
  combined_array = np.concatenate((prepend_array, differences))
  

  

  # Append 200 to the end
  ans = np.append(combined_array, 200)

  return ans

# Sample array
array = np.array([1, 3, 5, 7, 0])

# Print the original array
print("Original array:")
print(array)

# Calculate and print the differences
differences = calculate_differences(array)
print("\nDifference between neighboring elements, element-wise, and prepend [0, 0] and append[200] to the said array:")
print(differences)
