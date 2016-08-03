class Solution(object):
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0
        opt = [0] * len(grid[0])
        opt[0] = grid[0][0]
        for c in range(1, len(grid[0])):
            opt[c] = opt[c-1] + grid[0][c]
        for r in range(1, len(grid)):
            opt[0] += grid[r][0]
            for c in range(1, len(grid[0])):
                opt[c] = min(opt[c-1], opt[c]) + grid[r][c]
        return opt[-1]
