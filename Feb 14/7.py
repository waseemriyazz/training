import numpy as np

def find_zero_indices(array):
  """
  Finds the indices of elements equal to zero in a NumPy array.

  Args:
    array: A NumPy array.

  Returns:
    A NumPy array of indices where the elements are zero.
  """

  # Use np.where to find indices where elements are equal to zero
  zero_indices = np.where(array == 0)[0]

  return zero_indices

# Sample array
array = np.array([1, 0, 2, 0, 3, 0, 4, 5, 6, 7, 8])

# Print the original array
print("Original array:")
print(array)

# Find and print the indices of zero elements
zero_indices = find_zero_indices(array)
print("\nIndices of elements equal to zero:")
print(zero_indices)
