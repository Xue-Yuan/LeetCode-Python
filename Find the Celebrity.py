# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        can = n-1
        for i in range(n-1):
            if knows(can, i):
                can = i
        for i in range(n):
            if i != can:
                if not knows(i, can) or knows(can, i):
                    return -1
        return can
