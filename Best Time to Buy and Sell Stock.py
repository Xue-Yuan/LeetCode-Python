class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans, lowest = 0, sys.maxint
        for price in prices:
            lowest = min(price, lowest)
            ans = max(ans, price-lowest)
        return ans
