# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        b, e = 0, n
        while b < e:
            m = (b+e) >> 1
            if isBadVersion(m):
                e = m
            else:
                b = m+1
        return b
