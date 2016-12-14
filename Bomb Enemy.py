#MLE


class Node(object):
    def __init__(self):
        self.top = 0
        self.bottom = 0
        self.left = 0
        self.right = 0

    def sum(self):
        return self.top+self.bottom+self.left+self.right


class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0]) if grid else 0
        dp = [[Node() for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                node = dp[i][j]
                if grid[i][j] == 'W':
                    continue
                new = grid[i][j] == 'E'
                node.left = dp[i][j-1].left + new if j else new
                node.top = dp[i-1][j].top + new if i else new
        ans = 0
        for i in range(row)[::-1]:
            for j in range(col)[::-1]:
                node = dp[i][j]
                if grid[i][j] == 'W':
                    continue
                new = grid[i][j] == 'E'
                node.right = dp[i][j+1].right + new if j < col-1 else new
                node.bottom = dp[i+1][j].bottom + new if i < row-1 else new
                if grid[i][j] == '0':
                    ans = max(ans, node.sum())
        return ans
