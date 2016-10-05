class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odds = sum(v & 0x1 for k, v in collections.Counter(s).items())
        return len(s) - odds + (odds > 0)
