class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        bit, res = 0x1 << 16, 0
        while bit:
            res |= bit
            if res * res > x:
                res ^= bit
            bit >>= 1
        return res


class Solution2(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return x
        beg, end = 1, x
        while True:
            mid = beg + (end - beg) // 2
            if mid > x // mid:
                end = mid - 1
            else:
                if mid + 1 > x // (mid + 1):
                    return mid
                beg = mid + 1
