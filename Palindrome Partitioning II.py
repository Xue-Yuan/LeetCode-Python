class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        sz = len(s)
        pal = [[False] * sz for _ in range(sz)]
        opt = [sz] * sz
        for i in reversed(range(sz)):
            for j in range(i, sz):
                pal[i][j] = s[i] == s[j] and (i+2 >= j or pal[i+1][j-1])
                if pal[i][j]:
                    if j == sz-1:
                        opt[i] = 0
                    else:
                        opt[i] = min(opt[i], opt[j+1]+1)
        return opt[0]
