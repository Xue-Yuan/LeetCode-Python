class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
        slen = len(s)
        opt = [[False]*slen for _ in range(slen)]
        for r in range(slen-1, -1, -1):
            for c in range(r, slen):
                if r+2 >= c:
                    opt[r][c] = s[r] == s[c]
                else:
                    opt[r][c] = opt[r+1][c-1] and s[r] == s[c]

        def dfs(beg):
            if beg == slen:
                ret.append(path[:])
            else:
                for idx in range(beg, slen):
                    if opt[beg][idx]:
                        path.append(s[beg:idx+1])
                        dfs(idx+1)
                        path.pop()

        ret, path = [], []
        dfs(0)
        return ret
