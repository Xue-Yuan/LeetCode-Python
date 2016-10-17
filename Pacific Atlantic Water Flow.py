class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not any(matrix):
            return []
        row, col = len(matrix), len(matrix[0])
        pacific, atlantic, inf = 0x1, 0x2, float('inf')
        visited = [[0] * col for _ in range(row)]

        def _dfs(r, c, pre, ocean):
            if (not (0 <= r < row and 0 <= c < col) or
                    (visited[r][c] & ocean) == ocean or
                    matrix[r][c] < pre):
                return
            visited[r][c] |= ocean
            _dfs(r+1, c, matrix[r][c], ocean)
            _dfs(r, c+1, matrix[r][c], ocean)
            _dfs(r-1, c, matrix[r][c], ocean)
            _dfs(r, c-1, matrix[r][c], ocean)

        for i in range(row):
            _dfs(i, 0, -inf, pacific)
            _dfs(i, col-1, -inf, atlantic)
        for j in range(col):
            _dfs(0, j, -inf, pacific)
            _dfs(row-1, j, -inf, atlantic)

        return [(r, c) for r in range(row) for c in range(col) if visited[r][c] == pacific | atlantic]
