class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        for idx, citation in enumerate(citations+[0]):
            if idx+1 > citation:
                return idx
        return 0


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
        for i in reversed(range(sz+1)):
            h += cntr[i]
            if h >= i:
                return i
        return 0
