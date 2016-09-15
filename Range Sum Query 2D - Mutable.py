class BinaryIndexedTree(object):
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        self.matrix = matrix
        self.BIT = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                self._add(r+1, c+1, matrix[r][c])

    def _add(self, x, y, val):
        row, col = len(self.matrix), len(self.matrix[0])
        i = x
        while i <= row:
            j = y
            while j <= col:
                self.BIT[i][j] += val
                j += j & -j
            i += i & -i

    def update(self, x, y, val):
        self._add(x+1, y+1, val - self.matrix[x][y])
        self.matrix[x][y] = val

    def sum(self, row, col):
        ans, i = 0, row
        while i > 0:
            j = col
            while j > 0:
                ans += self.BIT[i][j]
                j -= j & -j
            i -= i & -i
        return ans


class NumMatrix(object):
    def __init__(self, matrix):
        self.tree = BinaryIndexedTree(matrix)

    def update(self, row, col, val):
        self.tree.update(row, col, val)

    def sumRegion(self, row1, col1, row2, col2):
        return (
            self.tree.sum(row2+1, col2+1) +
            self.tree.sum(row1, col1) -
            self.tree.sum(row1, col2+1) -
            self.tree.sum(row2+1, col1)
        )


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [5, 6, 7],
        [8, 9, 4],
    ]
    n = NumMatrix(matrix)
    print n.tree.matrix
    print n.sumRegion(0, 0, 2, 2)
    print n.sumRegion(1, 1, 2, 2)
    print n.sumRegion(2, 2, 2, 2)
    n.update(1, 2, 0)
    print n.tree.matrix
