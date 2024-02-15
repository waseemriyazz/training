import numpy as np

def find_nth_repetition_index(arr, n, target):
    indices = np.where(arr == target)[0]
    
    if len(indices) < n:
        return -1  # Not enough repetitions
    
    return indices[n - 1]

# User input for the array, n, and i
custom_array = np.array(input("Enter a space-separated array: ").split(), dtype=int)
n = int(input("Enter the value of n: "))
i = int(input("Enter the value of i: "))

# Find the index of the nth repetition of i
index_result = find_nth_repetition_index(custom_array, n, i)

# Display result
print("Array:", custom_array)
print(f"The index of the {n}th repetition of {i} is:", index_result)
