class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        f = s = t = float('inf')
        for num in nums:
            if num <= f:
                f = num
            elif num <= s:
                s = num
            elif num <= t:
                t = num
        return t != float('inf')
