class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        return self._getSkyline(buildings, 0, len(buildings))

    def _getSkyline(self, A, beg, end):
        if beg < end:
            if beg + 1 == end:
                l, r, h = A[beg][0], A[beg][1], A[beg][2]
                return [[l, h], [r, 0]]
            mid = (beg + end) >> 1
            first = self._getSkyline(A, beg, mid)
            second = self._getSkyline(A, mid, end)
            return self._merge(first, second)
        return []

    def _merge(self, A, B):
        ans = []
        i = j = h1 = h2 = 0
        while i < len(A) and j < len(B):
            if A[i][0] < B[j][0]:
                x, h1 = A[i][0], A[i][1]
                h = max(h1, h2)
                i += 1
            elif A[i][0] > B[j][0]:
                x, h2 = B[j][0], B[j][1]
                h = max(h1, h2)
                j += 1
            else:
                x, h1, h2 = A[i][0], A[i][1], B[j][1]
                h = max(h1, h2)
                i, j = i+1, j+1
            if not ans or ans[-1][1] != h:
                ans.append([x, h])
        ans += A[i:]
        ans += B[j:]
        return ans
