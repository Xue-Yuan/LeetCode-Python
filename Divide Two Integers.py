# Pretend we still have overflow in Python
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -(1 << 31), 0x7FFFFFFF
        if divisor == 0 or (dividend == INT_MIN and divisor == -1):
            return INT_MAX
        ret = 0
        positive = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                ret |= (1 << i)
                dividend -= (divisor << i)
        return ret if positive else -ret
