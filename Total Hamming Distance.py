class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for i in range(32):
            odd = even = 0
            for num in nums:
                if (num >> i) & 0x1:
                    odd += 1
                else:
                    even += 1
            total += odd * even
        return total
