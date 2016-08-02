class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        idx = len(s)-1
        while idx >= 0 and s[idx] == ' ':
            idx -= 1
        end = idx
        while idx >= 0 and s[idx] != ' ':
            idx -= 1
        return end - idx
