def search_insert_position(arr, m):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == m:
            return mid
        elif arr[mid] < m:
            low = mid + 1
        else:
            high = mid - 1

    return low

# Sample Input
arr = [1, 2, 4, 7]
m = 6
result = search_insert_position(arr, m)
print(result)
