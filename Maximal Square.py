class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        row, col = len(matrix), len(matrix[0])
        ans, opt = 0, [[0] * col for _ in range(row)]
        for c in range(0, col):
            opt[0][c] = 1 if matrix[0][c] == '1' else 0
            ans = max(ans, opt[0][c])
        for r in range(1, row):
            opt[r][0] = 1 if matrix[r][0] == '1' else 0
            for c in range(1, col):
                if matrix[r][c] == '1':
                    opt[r][c] = min(opt[r-1][c-1], opt[r-1][c], opt[r][c-1]) + 1
                ans = max(ans, opt[r][c])
        return ans**2


if __name__ == '__main__':
    matrix = [
        ['1', '0', '1', '0', '0'],
        ['1', '0', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '0', '0', '1', '0'],
    ]
    s = Solution()
    print s.maximalSquare(matrix)
