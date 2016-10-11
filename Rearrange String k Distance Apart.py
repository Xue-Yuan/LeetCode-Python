class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        if k <= 1:
            return str
        ans, h = [], [(-v, ch) for ch, v in collections.Counter(str).items()]
        heapq.heapify(h)
        while h:
            _h = []
            for _ in range(k):
                if not h:
                    if _h:
                        return ''
                    break
                v, ch = heapq.heappop(h)
                ans += ch,
                if -v > 1:
                    _h.append((v+1, ch))
            while _h:
                heapq.heappush(h, _h.pop())
        return ''.join(ans)
