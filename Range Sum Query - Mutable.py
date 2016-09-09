class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.BIT = [0] * (len(nums) + 1)
        self.nums = nums
        self.n = len(nums)
        for i in range(len(nums)):
            self._add(i + 1, nums[i])

    def _add(self, x, val):
        while x <= self.n:
            self.BIT[x] += val
            x += x & -x

    def _sum(self, x):
        res = 0
        while x > 0:
            res += self.BIT[x]
            x -= x & -x
        return res

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self._add(i + 1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._sum(j+1) - self._sum(i)
