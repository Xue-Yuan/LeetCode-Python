class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        opt = [1] + [0] * n
        for i in range(1, n+1):
            for j in range(i):
                opt[i] += opt[j] * opt[i-j-1]
        return opt[-1]
