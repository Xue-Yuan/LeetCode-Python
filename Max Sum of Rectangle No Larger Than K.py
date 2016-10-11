class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not any(matrix):
            return 0

        def maxSumSublist(vals):
            maxSum = float('-inf')
            prefixSum = 0
            prefixSums = [0]
            for val in vals:
                prefixSum += val
                i = bisect.bisect_left(prefixSums, prefixSum - k)
                if i < len(prefixSums):
                    maxSum = max(maxSum, prefixSum - prefixSums[i])
                bisect.insort(prefixSums, prefixSum)
            return maxSum

        maxSum = float('-inf')
        columns = zip(*matrix)
        for left in range(len(columns)):
            rowSums = [0] * len(matrix)
            for column in columns[left:]:
                rowSums = [r+c for r, c in zip(rowSums, column)]
                maxSum = max(maxSum, maxSumSublist(rowSums))
        return maxSum
