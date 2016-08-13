class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for c in nums:
            a = ~a&c|a&~c
        return a
