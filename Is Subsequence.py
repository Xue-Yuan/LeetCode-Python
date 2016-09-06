class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idx = 0
        for ch in s:
            idx = t.find(ch, idx)
            if idx < 0:
                return False
            idx += 1
        return True
