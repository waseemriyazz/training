def dutch(arr):
    n = len(arr)
    low = 0
    mid = 0
    high = n - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr

# Sample Input
arr1 = [0, 1, 2, 2, 1, 0]
arr2 = [0, 1, 2, 1, 2, 1, 2]

# Sample Output
print(dutch(arr1))  # Output: [0, 0, 1, 1, 2, 2]
print(dutch(arr2))