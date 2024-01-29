# 3.You are given an array of size ‘N’. The elements of the array are in the range from 1 to ‘N’.
# Ideally, the array should contain elements from 1 to ‘N’. But due to some miscalculations, there is a number R in the range [1, N] which appears in the array twice and another number M in the range [1, N] which is missing from the array.
# Your task is to find the missing number (M) and the repeating number (R).
# For example:
# Consider an array of size six. The elements of the array are { 6, 4, 3, 5, 5, 1 }. 
# The array should contain elements from one to six. Here, 2 is not present and 5 is occurring twice. Thus, 2 is the missing number (M) and 5 is the repeating number (R). 
# Follow Up
# Can you do this in linear time and constant additional space? 

def find_missing_and_repeating(arr):
    n = len(arr)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    expected_square_sum = sum(i**2 for i in range(1, n + 1))
    actual_square_sum = sum(i**2 for i in arr)

    missing_number = (expected_sum - actual_sum + actual_square_sum // actual_sum) // 2
    repeating_number = missing_number + actual_sum - expected_sum

    return missing_number, repeating_number

# Example usage:
arr = [6, 4, 3, 5, 5, 1]
missing, repeating = find_missing_and_repeating(arr)
print("Missing number:", missing)
print("Repeating number:", repeating)  

