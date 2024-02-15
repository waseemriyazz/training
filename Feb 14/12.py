import numpy as np

def euclidean_distance(a, b):
    distance = np.linalg.norm(np.array(a) - np.array(b))
    return distance

# Sample input
array_a = [1, 2, 3, 4, 5]
array_b = [4, 5, 6, 7, 8]

# Compute Euclidean distance
distance_result = euclidean_distance(array_a, array_b)

# Display result
print(f"Euclidean distance is: {distance_result:.4f}")
