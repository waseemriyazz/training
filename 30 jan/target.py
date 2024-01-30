def count_ways_to_achieve_target(arr, target):
    count = [0]

    def helper(index, current_sum):
        if index == len(arr):
            if current_sum == target:
                count[0] += 1
            return

        helper(index + 1, current_sum + arr[index])
        helper(index + 1, current_sum - arr[index])

    helper(0, 0)
    return count[0]

# Sample Input
arr = [1, 1, 1, 1, 1]
target = 3
result = count_ways_to_achieve_target(arr, target)
print(result)
