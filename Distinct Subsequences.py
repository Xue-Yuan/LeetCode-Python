class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        row, col = len(s)+1, len(t)+1
        opt = [[0] * col for _ in range(row)]
        opt[0][0] = 1
        for r in range(1, row):
            opt[r][0] = 1
            for c in range(1, col):
                opt[r][c] = opt[r-1][c]
                if s[r-1] == t[c-1]:
                    opt[r][c] += opt[r-1][c-1]
        return opt[-1][-1]
