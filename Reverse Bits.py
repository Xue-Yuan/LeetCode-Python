class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int('{:032b}'.format(n)[::-1], 2)
