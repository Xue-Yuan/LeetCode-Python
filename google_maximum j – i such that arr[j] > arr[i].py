"""Given an array arr[], find the maximum j – i such that arr[j] > arr[i]
"""


def solution(nums):
    sz = len(nums)
    s, b = [float('inf')]*sz, [float('-inf')] * sz
    for i in range(sz):
        s[i] = min(s[i], nums[i])
        b[~i] = max(b[~i], nums[~i])
    ans = i = j = 0
    while i < sz and j < sz:
        if b[j] > s[i]:
            ans = max(ans, j-i)
            j += 1
        else:
            i -= 1
    return ans
