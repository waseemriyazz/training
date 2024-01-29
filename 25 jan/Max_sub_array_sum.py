
def max_subarray_sum(arr):

    max_sum = float('-inf')
    current_sum = 0

    for num in arr:

        current_sum = max(num, current_sum + num)
       
        max_sum = max(max_sum, current_sum)


    return max_sum


arr = [1, 2, 7, -4, 3, 2, -10, 9, 1]
result = max_subarray_sum(arr)
print(result)