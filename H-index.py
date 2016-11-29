class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        b = 0
        sz = e = len(citations)
        while b < e:
            m = (b + e) >> 1
            if citations[m] >= sz-m:
                e = m
            else:
                b = m+1
        return sz - b


class Solution2(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        sz = len(citations)
        cntr = [0] * (sz+1)
        for c in citations:
            cntr[min(sz, c)] += 1
        h = 0
        for c in reversed(range(sz+1)):
            h += cntr[c]
            if h >= c:
                return c
        return 0
