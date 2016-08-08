class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy2 = 0
        sell1 = sell2 = -prices[0]
        ans = 0
        for price in prices:
            sell1 = max(sell1, -price)
            buy2, sell2 = max(sell1+price), max(sell2, buy2-price)
            ans = max(ans, sell2+price)
        return ans
