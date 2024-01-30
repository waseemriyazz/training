# 4.Search In Infinite Sorted 0-1 Array
# Problem statement
# You are given an infinite array consisting of only ones and zeroes, in sorted order. You have to find the index of the first occurrence of 1.

# Example:
# If the array is 0 0 0 0 1 1 1 1… then, the first occurrence of 1 will be at index 4 therefore the answer here is 4.
# Note:
# As the array size is infinite, the actual array won’t be given to you. Instead, you will be able to access the array elements by calling a method named ‘get’.

# get(i) : returns the value present at index I.

# Indexing is 0-based. 

# Instead of representing an infinite array in the input, we give the index of the first occurrence of 1 in the input itself. However, this input will be completely hidden from the user.

# It is guaranteed that the answer will fit in a 64-bit integer.

# pseudo code 
"""
the answer can be in between 0 and 2^64-1


"""


firstOccurence = int(input("This value is hidden from the user :"))

def binarySearch(key, start , end):
    while start <= end:
        mid = start + (end - start) // 2
        if mid == key:
            return mid
        elif mid < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1
calculated_index=binarySearch(firstOccurence, 0 , 2**64-1)
print(calculated_index)






