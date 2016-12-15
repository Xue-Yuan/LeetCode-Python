class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        sz = len(citations)
        b, e = 0, sz
        while b < e:
            m = (b+e) >> 1
            if citations[m] < sz-m:
                b = m+1
            else:
                e = m
        return sz-b
