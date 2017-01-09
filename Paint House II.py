"""Record the minimal two of the previous row so we don't need to
scan for the minimal, by which the time complexity O(nk) can be made.
"""


class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not any(costs):
            return 0
        row, col = len(costs), len(costs[0]) if costs else 0
        dp = [[0] * col for _ in range(row)]
        dp[0] = costs[0][:]
        for i in range(1, row):
            for j in range(col):
                dp[i][j] = min(dp[i-1][p] for p in range(col) if j != p) + costs[i][j]
        return min(dp[-1])
