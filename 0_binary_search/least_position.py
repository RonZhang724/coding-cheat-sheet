def find_rotate_index(nums, left, right):
    if nums[left] < nums[right]:
        return 0

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            return mid + 1
        else:
            if nums[mid] < nums[left]:
                right = mid - 1
            else:
                left = mid + 1


arr = [1, 2, 3, 0]
print(find_rotate_index(arr, 0, len(arr) - 1))
