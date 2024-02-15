import numpy as np

def remove_nan_values(array):
  """
  Removes NaN values from a NumPy array using two methods:

  1. Using np.dropna: This is the easiest and most efficient method.
  2. Using conditional indexing: This provides more control but might be less performant.

  Args:
    array: A NumPy array.

  Returns:
    A new NumPy array without NaN values.
  """

 
  filtered_array_indexing = array[~np.isnan(array)]

  print("Original array:")
  print(array)



  print("\nUsing conditional indexing")
  print(filtered_array_indexing)

# Sample array
array = np.array([200., 300., np.nan, np.nan, np.nan, 700.])

remove_nan_values(array)
