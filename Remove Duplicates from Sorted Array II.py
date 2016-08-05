class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cur = cnt = 1
        for idx in range(1, len(nums)):
            if nums[idx] == nums[cur-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt < 3:
                nums[cur] = nums[idx]
                cur += 1
        return cur


class Solution(object):
    idx = 0
    for num in nums:
        if idx < 2 or num > nums[idx-2]:
            nums[idx] = num
            idx += 1
    return idx
