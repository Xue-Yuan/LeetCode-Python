class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        row, col = len(matrix), len(matrix[0]) if matrix else 0
        self.prefix_sum = prefix = [[0] * (col+1) for _ in range(row+1)]
        for r in range(1, row+1):
            for c in range(1, col+1):
                prefix[r][c] = prefix[r][c-1] - prefix[r-1][c-1] + prefix[r-1][c] + matrix[r-1][c-1] 

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        prefix = self.prefix_sum
        return prefix[row2+1][col2+1] - prefix[row2+1][col1] - prefix[row1][col2+1] + prefix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
