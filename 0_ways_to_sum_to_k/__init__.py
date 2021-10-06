from collections import deque


def count_ways(nums, k):
    result = 0

    queue = deque()
    for num in nums:
        queue.append((num, num))

    while queue:
        cur_num, cur_sum = queue.popleft()
        if cur_sum == k:
            result += 1
        elif cur_sum > k:
            continue
        else:
            for num in nums:
                if num >= cur_num:
                    queue.append((num, cur_sum+num))
    return result



"""
1   1   1   1   1   1   1
1   1   1   1   3
1   3   3
7
"""
arr = [1, 3, 7]
k = 7

print(count_ways(arr, k))
