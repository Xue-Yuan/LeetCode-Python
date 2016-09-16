class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cntr = collections.Counter(s)
        return len(filter(lambda x: cntr[x] & 0x1, cntr)) <= 1
