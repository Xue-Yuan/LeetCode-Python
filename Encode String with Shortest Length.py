class Solution(object):
    def encode(self, s):
        memo = {}

        def _encode(s):
            if len(s) <= 3:
                return s
            if s not in memo:
                pos = (s+s).find(s, 1)
                if pos < len(s):
                    can = '{}[{}]'.format(len(s)/pos, _encode(s[:pos]))
                else:
                    can = s
                for m in range(1, len(s)):
                    new = _encode(s[:m]) + _encode(s[m:])
                    if len(new) < len(can):
                        can = new
                memo[s] = can
            return memo[s]

        return _encode(s)


class Solution2(object):
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        sz = len(s)
        dp = [[""] * (sz+1) for _ in range(sz+1)]
        for i in range(1, sz+1):
            for j in range(i, 0, -1):
                t = s[j-1:i]
                if len(t) <= 4:
                    dp[j][i] = t
                else:
                    pos = (t+t).find(t, 1)
                    if pos < len(t):
                        dp[j][i] = '{}[{}]'.format(len(t)/pos, dp[j][j+pos-1])
                    else:
                        dp[j][i] = t
                    for k in range(j, i):
                        t = dp[j][k] + dp[k+1][i]
                        if len(t) < len(dp[j][i]):
                            dp[j][i] = t
        return dp[1][sz]
