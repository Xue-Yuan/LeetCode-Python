class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        sz = len(strs)
        dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(sz+1)]
        for ith in range(1, sz+1):
            ones, zeros = strs[ith-1].count('1'), strs[ith-1].count('0')
            for _0 in range(m+1):
                for _1 in range(n+1):
                    if ones <= _1 and zeros <= _0:
                        dp[ith][_0][_1] = max(dp[ith-1][_0-zeros][_1-ones]+1, dp[ith-1][_0][_1])
                    else:
                        dp[ith][_0][_1] = dp[ith-1][_0][_1]
        return dp[sz][m][n]


class Solution2(object):
    def findMaxForm(self, strs, m, n):
        sz = len(strs)
        dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(2)]
        cur, pre = 0, 1
        for ith in range(1, sz+1):
            ones, zeros = strs[ith-1].count('1'), strs[ith-1].count('0')
            for _0 in range(m+1):
                for _1 in range(n+1):
                    if ones <= _1 and zeros <= _0:
                        dp[cur][_0][_1] = max(dp[pre][_0-zeros][_1-ones]+1, dp[pre][_0][_1])
                    else:
                        dp[cur][_0][_1] = dp[pre][_0][_1]
            cur, pre = pre, cur
        return dp[pre][m][n]


class Solution3(object):
    def findMaxForm(self, strs, m, n):
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for s in strs:
            ones, zeros = s.count('1'), s.count('0')
            for _0 in range(m+1)[::-1]:
                for _1 in range(n+1)[::-1]:
                    if ones <= _1 and zeros <= _0:
                        dp[_0][_1] = max(dp[_0-zeros][_1-ones]+1, dp[_0][_1])
        return dp[m][n]
