import numpy as np

def find_peaks(arr):
    peaks = np.where((arr[:-2] < arr[1:-1]) & (arr[1:-1] > arr[2:]))[0] + 1
    return peaks

# User input for custom array
custom_array = np.array(input("Enter a space-separated array: ").split(), dtype=int)

# Find peaks
peaks_result = find_peaks(custom_array)

# Display result
print("Array:", custom_array)
print("Positions of peak values:", peaks_result)
