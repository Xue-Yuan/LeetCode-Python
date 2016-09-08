"""
Get the last bit of n: n & -n
Get rid of the last bit of n: n & (n-1)
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        separator = 0
        for num in nums:
            separator ^= num
        separator &= -separator
        first = second = 0
        for num in nums:
            if num & separator:
                first ^= num
            else:
                second ^= num
        return [first, second]
