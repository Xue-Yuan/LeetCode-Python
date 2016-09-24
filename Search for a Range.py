class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = self._lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = self._lower_bound(nums, target+1)
        return [start, end-1]

    def _lower_bound(self, nums, target):
        b, e = 0, len(nums)
        while b < e:
            m = (b + e) >> 1
            if nums[m] < target:
                b = m+1
            else:
                e = m
        return b
