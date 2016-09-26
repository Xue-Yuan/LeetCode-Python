class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = buy2 = 0
        sell1 = sell2 = -sys.maxint
        for p in prices:
            sell1 = max(sell1, -p)
            buy2 = max(sell1+p, buy2)
            sell2 = max(sell2, buy2-p)
            ans = max(ans, sell2+p)
        return ans
