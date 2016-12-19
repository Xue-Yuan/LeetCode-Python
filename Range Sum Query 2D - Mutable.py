class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.row = row = len(matrix)
        self.col = col = len(matrix[0]) if matrix else 0
        self.sum = [[0] * (col+1) for _ in range(row+1)]
        for r in range(row):
            for c in range(col):
                self._add(r+1, c+1, matrix[r][c])

    def _add(self, r, c, val):
        x = r
        while x <= self.row:
            y = c
            while y <= self.col:
                self.sum[x][y] += val
                y += y & -y
            x += x & -x

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        self._add(row+1, col+1, val - self.matrix[row][col])
        self.matrix[row][col] = val

    def _sum(self, r, c):
        ans, x = 0, r
        while x > 0:
            y = c
            while y > 0:
                ans += self.sum[x][y]
                y -= y & -y
            x -= x & -x
        return ans

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        _sum = self._sum
        return (
            _sum(row2+1, col2+1) -
            _sum(row1, col2+1) -
            _sum(row2+1, col1) +
            _sum(row1, col1)
        )


class NumMatrix2(object):
    """O(n) time update and query
    """
    def __init__(self, matrix):
        rows, cols = len(matrix), len(matrix[0]) if matrix else 0
        sum_matrix = [[0] * (cols+1)]
        for row in matrix:
            sum_row = [0]
            for col in row:
                sum_row.append(sum_row[-1] + col)
            sum_matrix.append(sum_row)
        self.sum_matrix = sum_matrix

    def update(self, row, col, val):
        diff = val - (self.sum_matrix[row+1][col+1] - self.sum_matrix[row+1][col])
        cols = len(self.sum_matrix[0])
        for c in range(col+1, cols):
            self.sum_matrix[row+1][c] += diff

    def sumRegion(self, row1, col1, row2, col2):
        ans = 0
        for r in range(row1+1, row2+2):
            ans += self.sum_matrix[r][col2+1] - self.sum_matrix[r][col1]
        return ans


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [5, 6, 7],
        [8, 9, 4],
    ]
    n = NumMatrix(matrix)
    print n.sumRegion(0, 0, 2, 2)
    print n.sumRegion(1, 1, 2, 2)
    print n.sumRegion(2, 2, 2, 2)
    n.update(1, 2, 0)
    print n.matrix
