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


class Solution2(object):
    def maxProfit(self, prices):
        ans = 0
        for nxt, cur in zip(prices[1:], prices):
            if nxt > cur:
                ans += nxt - cur
        return ans
