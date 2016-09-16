"""Record the minimal two of the previous row so we don't need to
scan for the minimal, by which the time complexity O(nk) can be made.
"""


class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        n, k = len(costs), len(costs[0])
        opt = [costs[0][:]] + [[0] * k for _ in range(n-1)]
        for i in range(1, n):
            for j in range(k):
                cost = costs[i][j] + opt[i-1][(j+1)%k]
                for m in range(k):
                    if j != m:
                        cost = min(cost, opt[i-1][m]+costs[i][j])
                opt[i][j] = cost
        return min(opt[-1])
