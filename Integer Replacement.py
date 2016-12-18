class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        while n > 1:
            if n & 0x1:
                if n & 0x3 == 0x3 and n != 3:
                    n += 1
                else:
                    n -= 1
            else:
                n >>= 1
            total += 1
        return total
