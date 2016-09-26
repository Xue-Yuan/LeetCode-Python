class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not k:
            return 0
        if k >= len(prices):
            ans = 0
            for nxt, cur in zip(prices[1:], prices):
                if nxt > cur:
                    ans += nxt - cur
            return ans
        final = 0
        buys, sells = [0] * k, [-sys.maxint] * k
        for p in prices:
            for i in range(1, 2*k):
                idx = i >> 1
                if i & 0x1:
                    sells[idx] = max(buys[idx]-p, sells[idx])
                else:
                    buys[idx] = max(buys[idx], sells[idx-1]+p)
            final = max(final, sells[-1]+p)
        return max(max(sells), final)
