class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        opt = [True] + [False] * len(s)
        for i in range(1, len(s)+1):
            for j in range(i+1):
                if opt[j] and s[j:i] in wordDict:
                    opt[i] = True
                    break
        return opt[-1]
