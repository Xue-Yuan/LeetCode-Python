class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        b = ret = 0
        m = {}
        for i, ch in enumerate(s):
            if ch in m:
                b = max(b, m[ch]+1)
            ret = max(ret, i-b+1)
            m[ch] = i
        return ret
