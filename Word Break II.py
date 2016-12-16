class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        memo = {}

        def dfs(s):
            if s not in memo:
                ans = []
                for i in range(1, len(s)):
                    if s[:i] in wordDict:
                        for rest in dfs(s[i:]):
                            ans.append(s[:i] + ' ' + rest)
                if s in wordDict:
                    ans.append(s)
                memo[s] = ans
            return memo[s]

        return dfs(s)
