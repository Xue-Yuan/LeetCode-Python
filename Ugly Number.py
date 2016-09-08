class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num > 0:
            for prime in (2, 3, 5):
                while not num % prime:
                    num /= prime
        return num == 1
