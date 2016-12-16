class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [float('-inf')] + nums + [float('-inf')]
        b, e = 1, len(nums)
        while b < e:
            m = (b+e) >> 1
            if nums[m-1] < nums[m] > nums[m+1]:
                return m-1
            if nums[m-1] < nums[m] < nums[m+1]:
                b = m+1
            else:
                e = m
        return -1
