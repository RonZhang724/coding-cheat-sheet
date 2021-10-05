def binary_search(nums, left, right, target):

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [0, 2, 3, 4, 5]
print(binary_search(arr, 0, len(arr)-1, 4))
