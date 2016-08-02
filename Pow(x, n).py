class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        neg, n = n < 0, abs(n)
        ret = 1.
        while n:
            if n & 0x1:
                ret *= x
            x *= x
            n >>= 1
        return ret if not neg else 1/ret
