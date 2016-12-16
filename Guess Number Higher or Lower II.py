class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}

        def guess(beg, end):
            if (beg, end) not in memo:
                if beg >= end:
                    return 0
                ans = float('inf')
                for i in range(beg, end+1):
                    ans = min(ans, max(guess(beg, i-1), guess(i+1, end))+i)
                memo[beg, end] = ans
            return memo[beg, end]

        return guess(1, n)
