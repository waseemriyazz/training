import numpy as np

def get_unique_elements(array):
 """
 Returns the unique elements of a NumPy array.

 Args:
   array: A NumPy array.

 Returns:
   A NumPy array containing the unique elements of the input array.
 """

 # Use np.unique to get unique elements
 unique_elements = np.unique(array)

 return unique_elements

# Example usage
array1 = np.array([10, 10, 20, 20, 30, 30])
array2 = np.array([[1, 1], [2, 3]])

print("Original array:")
print(array1)
print("Unique elements of the above array:")
print(get_unique_elements(array1))

print("\nOriginal array:")
print(array2)
print("Unique elements of the above array:")
print(get_unique_elements(array2))