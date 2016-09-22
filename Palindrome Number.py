class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        r_x, tmp = 0, x
        while tmp:
            r_x = r_x*10 + tmp%10
            tmp /= 10
        return r_x == x
