class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        if len(p) > 1 and p[1] == '*':
            return (
                self.isMatch(s, p[2:]) or
                bool(s) and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p)
                )
        return bool(s) and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])


class Solution2(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sz_s, sz_p = len(s), len(p)
        opt = [[False] * (sz_p+1) for _ in range(sz_s+1)]
        opt[0][0] = True
        for j in range(2, sz_p+1):
            opt[0][j] = opt[0][j-2] and p[j-1] == '*'
        for i in range(1, sz_s+1):
            for j in range(1, sz_p+1):
                if p[j-1] != '*':
                    opt[i][j] = opt[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                else:
                    opt[i][j] = opt[i][j-2] or (opt[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
        return opt[sz_s][sz_p]
