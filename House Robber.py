class Solution2(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob = skip = 0
        for num in nums:
            rob, skip = skip+num, max(rob, skip)
        return max(rob, skip)
