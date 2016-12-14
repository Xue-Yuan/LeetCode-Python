class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not any(matrix):
            return 0
        row, col = len(matrix), len(matrix[0]) if matrix else 0
        memo = [[1] * col for _ in range(row)]

        def dfs(r, c, pre):
            if not (0 <= r < row and 0 <= c < col) or pre >= matrix[r][c]:
                return 0
            if memo[r][c] > 1:
                return memo[r][c]
            cur = matrix[r][c]
            memo[r][c] += max(
                dfs(r+1, c, cur),
                dfs(r-1, c, cur),
                dfs(r, c+1, cur),
                dfs(r, c-1, cur)
            )
            return memo[r][c]

        return max(
            dfs(r, c, float('-inf'))
            for r in range(row)
            for c in range(col)
        )
