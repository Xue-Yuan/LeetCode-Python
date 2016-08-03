class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        opt = [1] * n
        for r in range(1, m):
            for c in range(1, n):
                opt[c] = opt[c] + opt[c-1]
        return opt[-1]
