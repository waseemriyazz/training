import numpy as np

def sort_array(array, axis):
  """
  Sorts a NumPy array along the specified axis.

  Args:
    array: A NumPy array.
    axis: The axis along which to sort. 0 for first axis, -1 for last axis.

  Returns:
    A new NumPy array sorted along the specified axis.
  """

  # Make a copy to avoid modifying the original array
  sorted_array = array.copy()

