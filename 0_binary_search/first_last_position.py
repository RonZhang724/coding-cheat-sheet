def find_first_pos(nums, left, right, target):

    first_position = -1  # keep track of the latest valid mid position
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            first_position = mid
            right = mid - 1  # continue searching to the left
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return first_position


def find_last_pos(nums, left, right, target):

    last_position = -1  # keep track of the latest valid mid position
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            last_position = mid
            left = mid + 1  # continue searching to the right
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return last_position


arr = [0, 1, 2, 2, 2, 2, 3]
print(find_first_pos(arr, 0, len(arr)-1, 2))
print(find_last_pos(arr, 0, len(arr)-1, 2))
