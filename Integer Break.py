class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        opt = [1] * (n+1)
        for i in range(2, n+1):
            for j in range(1, i/2+1):
                opt[i] = max(opt[i], max(j, opt[j])*max(i-j, opt[i-j]))
        return opt[n]
