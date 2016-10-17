# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        b, e = 1, n+1
        while b < e:
            m = (b+e) >> 1
            if guess(m) > 0:
                b = m+1
            else:
                e = m
        return b
