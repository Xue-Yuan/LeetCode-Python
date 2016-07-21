class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        b, e = 0, len(nums)
        while b < e:
            m = ((e-b) >> 1) + b
            if nums[m] < target:
                b = m+1
            else:
                e = m
        return b
