def luckyNumber(n):
    if n <= 3:
        return [1]
    idx = 1
    nums = range(1, n+1, 2)
    while idx < len(nums):
        skip = nums[idx]
        if skip > len(nums):
            break
        del nums[skip-1::skip]
        idx += 1
    return nums
