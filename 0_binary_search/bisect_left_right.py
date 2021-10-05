def bisect_left(nums, left, right, x):
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left


def bisect_right(nums, left, right, x):
    while left < right:
        mid = (left + right) // 2
        if x < nums[mid]:
            right = mid
        else:
            left = mid + 1
    return left


arr = [1, 2, 2, 3, 4]
print(bisect_left(arr, 0, len(arr), 6))
print(bisect_right(arr, 0, len(arr), 2))
