def rotate_left(arr):
    n = len(arr)
    
   
    if n <= 1:
        return arr

    first_element = arr[0]


    for i in range(1, n):
        arr[i - 1] = arr[i]

    arr[n - 1] = first_element

    return arr
a = 5
arr = [1, 2, 3, 4, 5]
result = rotate_left(arr)
print(result)