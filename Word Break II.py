class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        m = collections.defaultdict(list)
        m[""] = [""]
        def dfs(s):
            if s not in m:
                for idx in range(1, len(s)+1):
                    word = s[:idx]
                    if word in wordDict:
                        for res in dfs(s[idx:]):
                            m[s].append(word + ' ' + res if res else word)
            return m[s]
        return dfs(s)
