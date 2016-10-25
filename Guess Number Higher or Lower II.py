class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}

        def min_val(b, e):
            if b >= e:
                return 0
            if (b, e) in memo:
                return memo[b, e]
            ans = float('inf')
            for i in range(b, e+1):
                ans = min(ans, i+max_val(b, i, e))
            memo[b, e] = ans
            return ans

        def max_val(b, i, e):
            return max(min_val(b, i-1), min_val(i+1, e))

        return min_val(1, n)
