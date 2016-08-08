class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        sell, ans = -prices[0], 0
        for price in prices:
            sell, ans = max(sell, -price), max(ans, sell+price)
        return ans
