class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        m = {'6': '9', '9': '6', '8': '8', '1': '1', '0': '0'}
        for i, n in enumerate(num):
            if n not in m or m[n] != num[~i]:
                return False
        return True
