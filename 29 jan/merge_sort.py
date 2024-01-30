# 3 4 1 6 2 5 7
# 
# 4 3 1 2
size1 = int(input("Enter the number of elements in array 1 "))
myList1 = []


print("Enter the elements of 1st array ")
for i in range(0, size1):
    i = int(input())
    myList1.append(i)

size2 = int(input("Enter the number of elements in array 2 "))
myList2 = [] 

print("Enter the elements of 2nd array ")
for i in range(0, size2):
    i = int(input())
    myList2.append(i)

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        return merge(merge_sort(left), merge_sort(right))

def merge(left_array, right_array):
    index_left = 0
    index_right = 0
    merged_arr = []
    while index_left < len(left_array) and index_right < len(right_array):
        if left_array[index_left] <= right_array[index_right]:
            merged_arr.append(left_array[index_left])
            index_left += 1
        else:
            merged_arr.append(right_array[index_right])
            index_right += 1
    
    while index_left < len(left_array):
        merged_arr.append(left_array[index_left])
        index_left += 1

    while index_right < len(right_array):
        merged_arr.append(right_array[index_right])
        index_right += 1

    return merged_arr


ans1 = merge_sort(myList1)
ans2 = merge_sort(myList2)

ans = set()
for i in ans1:
    ans.add(i)
for i in ans2:
    ans.add(i)
print(ans)

    
