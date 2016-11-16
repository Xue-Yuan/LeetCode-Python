class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def lower_bound(b, e, target):
            while b < e:
                m = (b+e) >> 1
                if nums[m] < target:
                    b = m+1
                else:
                    e = m
            return b
        first = lower_bound(0, len(nums), target)
        second = lower_bound(0, len(nums), target+1)
        if first == second:
            return [-1, -1]
        return [first, second-1]
