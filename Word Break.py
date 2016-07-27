class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        opt = [True] + [False for _ in s]
        for end in xrange(1, len(s)+1):
            for beg in xrange(end-1, -1, -1):
                opt[end] = opt[beg] and s[beg:end] in wordDict
                if opt[end]:
                    break
        return opt[-1]
