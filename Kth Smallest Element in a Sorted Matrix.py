import heapq


class Solution:
    '''Similar to merge k sorted arrays.
    '''

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row, col = len(matrix), len(matrix[0])
        heap = []
        for r in range(row):
            heap.append((matrix[r][0], r, 0))
        heapq.heapify(heap)
        ans = 0
        for _ in range(k):
            ans, r, c = heapq.heappop(heap)
            if c + 1 != col:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
        return ans
