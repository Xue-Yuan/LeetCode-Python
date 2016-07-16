class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def lcp(s, t):
            for i in range(0, min(len(s), len(t))):
                if s[i] != t[i]:
                    return t[:i]
            return s[0:len(t)]
        return reduce(lcp, strs) if strs else ''
