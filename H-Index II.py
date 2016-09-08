class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        ans, l = 0, len(citations)
        beg, end = 0, l
        while beg < end:
            mid = (beg + end) >> 1
            if citations[mid] >= l - mid:
                ans = max(ans, l - mid)
                end = mid
            else:
                ans = max(ans, citations[mid])
                beg = mid+1
        return ans
