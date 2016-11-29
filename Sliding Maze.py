#coding: utf-8


"""sliding maze。 一个迷宫，一个球， 球一直走直到遇到障碍物才能停下（up, down, left, right）。
问这个迷宫是不是solvable， followup 找最短操作。"""


from collections import deque


def sliding_maze(maze, start_pos, end_pos):
    """maze: (x, y): wall
    """
    UP, LEFT, DOWN, RIGHT = range(4)
    DELTA = ((-1, 0), (0, -1), (1, 0), (0, 1))
    row, col = len(maze), len(maze[0])
    WALL = 1

    def clc_90(drc):
        return (drc+1) & 0x3

    def c_clc_90(drc):
        return (drc+3) & 0x3

    def advance(cur, drc):
        nx, ny = map(sum, zip(cur, DELTA[drc]))
        if not (0 <= nx < row and 0 <= ny < col) or maze[nx, ny] == WALL:
            return cur, False
        return (nx, ny), True

    vistied = set()
    q = deque((start_pos, UP), (start_pos, DOWN), (start_pos, LEFT), (start_pos, RIGHT))
    cnt = 0
    while q:
        sz = len(q)
        for _ in range(sz):
            cur, drc = q.pop_left()
            if cur == end_pos:
                return cnt
            vistied.add(cur)
            while True:
                cur, dead = advance(cur, drc)
                if dead:
                    break
            if cur not in vistied:
                q.append((cur, clc_90(drc)))
                q.append((cur, c_clc_90(drc)))
        cnt += 1
    return -1
