class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        opt = [0, k, k*k]
        for _ in range(n-1):
            opt.append((opt[-1]+opt[-2])*(k-1))
        return opt[n]
