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


class Solution2(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n in (0, 1):
            return (1, x)[n]
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        tmp = self.myPow(x, n/2)
        if n & 0x1:
            return tmp * tmp * x
        else:
            return tmp * tmp
