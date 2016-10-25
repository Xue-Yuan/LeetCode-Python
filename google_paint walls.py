#coding: utf-8


"""给一个矩阵，1是墙，高度是一，0是空地，问给所有墙外围，涂上颜色，要多少单位的油漆。
例子： 1111  涂:   1111
      0001           1
的话，就是12， 有12个边要涂，follow 是一个迷宫，中间可能有不连通的区域，问一个油
漆匠从一个入口进入，能涂多少单位油漆
"""


def paint_wall(grid):
    if not any(grid):
        return 0
    row, col = len(grid), len(grid[0])

    def check(r, c):
        cnt = 0
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if not (0 <= nr < row and 0 <= nc < col) or grid[nr][nc] == 0:
                cnt += 1
        return cnt

    return sum(check(r, c) for r in range(row) for c in range(col) if grid[r][c])


def follow_up(grid):
    """DFS
    """
    pass


if __name__ == '__main__':
    grid = [
        [1,1,1,1],
        [0,0,0,1],
    ]
    print paint_wall(grid)
