class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, cool, sell = 0, 0, -sys.maxint
        for p in prices:
            buy, sell, cool = max(buy, cool), max(sell, buy-p), sell+p
        return max(buy, sell, cool)
