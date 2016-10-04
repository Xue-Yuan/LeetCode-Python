class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        reachable, ans = 0, float('inf')
        row, col = len(grid), len(grid[0]) if grid else 0
        total = [[0] * col for _ in range(row)]
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    ans = float('inf')
                    q = collections.deque([(r, c, 0)])
                    while q:
                        x, y, dis = q.popleft()
                        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                            n_x, n_y = x+dx, y+dy
                            if 0 <= n_x < row and 0 <= n_y < col and grid[n_x][n_y] == reachable:
                                q.append((n_x, n_y, dis+1))
                                total[n_x][n_y] += dis+1
                                ans = min(ans, total[n_x][n_y])
                                grid[n_x][n_y] -= 1
                    reachable -= 1
        return ans if ans != float('inf') else -1
