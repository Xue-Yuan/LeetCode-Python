class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        def dfs(s):
            if s not in m:
                m[s] = []
                for idx in range(1, len(s)+1):
                    if s[:idx] in wordDict:
                        for res in dfs(s[idx:]):
                            m[s].append(s[:idx]+' '+res if res else s[:idx])
            return m[s]
        m = {"": [""]}
        return dfs(s)
