def previous_permutation(nums):
    sz = len(nums)
    for i in range(sz-1, -1, -1):
        if i > 0 and nums[i-1] > nums[i]:
            for j in range(sz-1, -1, -1):
                if nums[j] < nums[i-1]:
                    nums[j], nums[i-1] = nums[i-1], nums[j]
                    break
            break
    nums[i:] = nums[i:][::-1]
