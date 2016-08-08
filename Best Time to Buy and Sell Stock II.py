class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy, sell = 0, -prices[0]
        for price in prices:
            buy, sell = max(buy, sell+price), max(sell, buy-price)
        return buy
