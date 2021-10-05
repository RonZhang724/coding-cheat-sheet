def find_left_border(nums, left, right, target):

    left_border = -1  # keep track of the latest smaller number
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left_border = mid
            left = mid + 1
        else:  # in case arr[mid] >= target
            right = mid - 1

    return left_border


def find_right_border(nums, left, right, target):
    left = 0
    right = len(nums) - 1

    right_border = -1  # keep track of the latest larger number
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right_border = mid
            right = mid - 1

    return right_border


arr = [1, 2, 2, 2, 4, 5, 7]
print(find_left_border(arr, 0, len(arr)-1, 2))
print(find_right_border(arr, 0, len(arr)-1, 2))
