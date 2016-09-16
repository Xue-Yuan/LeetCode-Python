class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        for i in range(1, len(costs)):
            for j in range(3):
                cost = sys.maxint
                for k in range(3):
                    if j != k:
                        cost = min(cost, costs[i-1][k] + costs[i][j])
                costs[i][j] = cost
        return min(costs[-1])
