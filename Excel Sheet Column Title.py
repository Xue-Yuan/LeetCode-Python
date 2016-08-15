class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        while n:
            n, re = divmod(n-1, 26)
            ans += chr(65+re)
        return ans[::-1]
