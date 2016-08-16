class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre1 = pre2 = 0
        for num in nums:
            pre1, pre2 = max(pre2+num, pre1), pre1
        return pre1
