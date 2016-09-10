class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        row, col = len(matrix), len(matrix[0])
        def _dfs(r, c, pre):
            if 0 <= r < row and 0 <= c < col and (pre is None or matrix[r][c] > pre):
                if length[r][c] == 1:
                    length[r][c] = max(
                        _dfs(r+1, c, matrix[r][c]),
                        _dfs(r-1, c, matrix[r][c]),
                        _dfs(r, c+1, matrix[r][c]),
                        _dfs(r, c-1, matrix[r][c]),
                    ) + 1
                return length[r][c]
            return 0
        length = [[1] * col for _ in range(row)]
        return max(_dfs(i, j, None) for i in range(row) for j in range(col))


if __name__ == '__main__':
    nums = [
      [9,9,4],
      [6,6,8],
      [2,1,1]
    ]
    print Solution().longestIncreasingPath(nums)
    nums = [
        [13,5,13,9],
        [5,0,2,9],
        [10,13,11,10],
        [0,0,13,13],
    ]
    print Solution().longestIncreasingPath(nums)
