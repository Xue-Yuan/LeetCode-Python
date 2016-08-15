class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for ch in s:
            ans = ans*26 + ord(ch)-64
        return ans
