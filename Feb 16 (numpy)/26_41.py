# 26. Write a NumPy program to find the number of rows and columns of a given matrix.
import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

rows, columns = matrix.shape
print("Number of rows:", rows)
print("Number of columns:", columns)

# 27. Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1, the rest are 0.
identity_matrix = np.identity(3)
print("3x3 Identity Matrix:")
print(identity_matrix)

# 28. Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.
border_matrix = np.ones((10, 10))
border_matrix[1:-1, 1:-1] = 0
print("10x10 Matrix with borders of 1 and inside of 0:")
print(border_matrix)

# 29. Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.
diagonal_matrix = np.diag([1, 2, 3, 4, 5])
print("5x5 Matrix with diagonal elements 1, 2, 3, 4, 5:")
print(diagonal_matrix)

# 30. Write a NumPy program to create an 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal.
staggered_matrix = np.zeros((4, 4))
staggered_matrix[::2, 1::2] = 1
staggered_matrix[1::2, ::2] = 1
print("4x4 Matrix with staggered 0 and 1:")
print(staggered_matrix)

# 31. Write a NumPy program to create a 3x3x3 array filled with arbitrary values.
arbitrary_array = np.random.random((3, 3, 3))
print("3x3x3 Array filled with arbitrary values:")
print(arbitrary_array)

# 32. Write a NumPy program to compute sum of all elements, sum of each column and sum of each row of an given array.
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print("Sum of all elements:", np.sum(array))
print("Sum of each column:", np.sum(array, axis=0))
print("Sum of each row:", np.sum(array, axis=1))

# 33. Write a NumPy program to compute the inner product of two given vectors.
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
inner_product = np.dot(vector1, vector2)
print("Inner product of vectors:", inner_product)

# 34. Write a NumPy program to add a vector to each row of a given matrix.
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
vector = np.array([7, 8, 9])
result_matrix = matrix + vector
print("Result matrix:")
print(result_matrix)

# 35. Write a NumPy program to save a given array to a binary file.
array = np.array([1, 2, 3, 4, 5])
np.save("array_file.npy", array)

# 36. Write a NumPy program to save two given arrays into a single file in compressed format (.npz format) and load it.
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
np.savez_compressed("arrays_file.npz", array1=array1, array2=array2)
loaded_data = np.load("arrays_file.npz")
print("Loaded array1:", loaded_data['array1'])
print("Loaded array2:", loaded_data['array2'])

# 37. Write a NumPy program to save a given array to a text file and load it.
array = np.array([[1, 2, 3],
                  [4, 5, 6]])
np.savetxt("array_file.txt", array)
loaded_array = np.loadtxt("array_file.txt")
print("Loaded array from text file:")
print(loaded_array)

# 38. Write a NumPy program to convert a given array into bytes, and load it as array.
array = np.array([1, 2, 3, 4, 5])
bytes_array = array.tobytes()
loaded_array = np.frombuffer(bytes_array, dtype=array.dtype)
print("Loaded array from bytes:")
print(loaded_array)

# 39. Write a NumPy program to convert a given array into a list and then convert it into a list again.
array = np.array([1, 2, 3, 4, 5])
list_array = array.tolist()
converted_array = np.array(list_array)
print("Converted array:")
print(converted_array)

# 40. Write a NumPy program to compute the x and y coordinates for points on a sine curve and plot the points using matplotlib.
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Curve')
plt.show()

# 41. Write a NumPy program to convert numpy dtypes to native python types.
array = np.array([1, 2, 3, 4, 5])
native_types = array.tolist()
print("Native Python types:", native_types)