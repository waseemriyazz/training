import numpy as np

def get_sorted_indices(array):
  """
  Gets the indices of the sorted elements of a given NumPy array.

  Args:
    array: A NumPy array.

  Returns:
    A NumPy array containing the indices of the sorted elements.
  """

  # Get the indices of the elements in the sorted order
  sorted_indices = np.argsort(array)

  return sorted_indices

# Sample array
array = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])

# Print the original array
print("Original array:")
print(array)

# Get and print the sorted indices
sorted_indices = get_sorted_indices(array)
print("\nIndices of the sorted elements of a given array:")
print(sorted_indices)
