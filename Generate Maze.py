import random


def generateMaze(row, col):
    maze = [[-1] * col for _ in range(row)]

    def dfs(r, c):
        if not (0 <= r < row and 0 <= c < col) or maze[r][c] >= 0:
            return False
        maze[r][c] = 0
        if r == row-1 and c == col-1:
            return True
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while d:
            idx = random.randint(0, len(d)-1)
            dr, dc = d.pop(idx)
            if dfs(r+dr, c+dc):
                return True
        maze[r][c] = 1
        return False

    dfs(0, 0)
    for r in range(row):
        for c in range(col):
            if maze[r][c] != 0:
                maze[r][c] = random.randint(0, 1)

    return maze


if __name__ == '__main__':
    maze = generateMaze(10, 15)
    for r in maze:
        print ''.join(map(str, r))
