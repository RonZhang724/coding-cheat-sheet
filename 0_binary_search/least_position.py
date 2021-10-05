def find_rotate_index(nums, left, right):
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1
    return left


def find_rotate_index_with_duplicates(nums, left, right):
    while left < right:
        mid = (left + right) // 2
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[mid] <= nums[right]:
            right = mid
        else:
            left = mid + 1
    return left


arr = [1, 2, 3, 0]
print(find_rotate_index(arr, 0, len(arr) - 1))

arr = [1]
print(find_rotate_index(arr, 0, len(arr) - 1))

arr = [3, 1, 3, 3, 3]
print(find_rotate_index_with_duplicates(arr, 0, len(arr) - 1))
