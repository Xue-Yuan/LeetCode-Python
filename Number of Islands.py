#https://discuss.leetcode.com/topic/16749/7-lines-python-14-lines-java


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0]) if grid else 0

        def dfs(r, c):
            if 0 <= r < row and 0 <= c < col and grid[r][c] == '1':
                grid[r][c] = '0'
                map(dfs, (r+1, r-1, r, r), (c, c, c+1, c-1))
                return 1
            return 0

        return sum(dfs(r, c) for r in range(row) for c in range(col))
