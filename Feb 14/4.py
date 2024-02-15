import numpy as np

def count_occurrences(array, item):
  """
  Counts the occurrences of a specified item in a NumPy array.

  Args:
    array: A NumPy array.
    item: The item to count occurrences of.

  Returns:
    The number of occurrences of the item in the array.
  """

  # Use np.count_nonzero to count occurrences efficiently
  count = np.count_nonzero(array == item)

  return count

# Sample array
array = np.array([10, 20, 20, 20, 20, 0, 20, 30, 30, 30, 0, 0, 20, 20, 0])

# Print the original array
print("Original array:")
print(array)

# Items to count
items_to_count = [10, 20, 30, 0]

# Count occurrences of each item and print results
for item in items_to_count:
  count = count_occurrences(array, item)
  print(f"Count of {item} in the array: {count}")
