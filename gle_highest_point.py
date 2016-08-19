#coding: utf-8
"""
Given a heatmap which is a 3 dimension matrix and define a movement rule:
a point on the heatmap can only go down hill. Ask: given some points on
the heatmap, find out the higest point that can meet all the given points.
说白了就是给个矩阵，上面都有自己的value，然后movement规定了只能从大的value走到小
的value，然后再给几个点，问可以到这些点的最高的点是哪一个。
"""


def solution(matrix, points):
    if not matrix or not matrix[0]:
        return None
    row, col = len(matrix), len(matrix[0])
    record = [[0] * col for _ in range(row)]

    def dfs(r, c, pre):
        if 0 <= r < row and 0 <= c < col and not visited[r][c] and matrix[r][c] > pre:
            record[r][c] += 1
            visited[r][c] = True
            dfs(r+1, c, matrix[r][c])
            dfs(r-1, c, matrix[r][c])
            dfs(r, c+1, matrix[r][c])
            dfs(r, c-1, matrix[r][c])

    for r, c in points:
        visited = [[False] * col for _ in range(row)]
        dfs(r, c, -1)

    ans = points[0]
    for r in range(row):
        for c in range(col):
            if record[r][c] == len(points):
                if matrix[r][c] > matrix[ans[0]][ans[1]]:
                    ans = (r, c)
    return ans


if __name__ == '__main__':
    matrix = [
        [1, 5, 3, 2],
        [9, 3, 8, 2],
        [9, 4, 8, 9],
        [0, 3, 2, 3],
    ]
    points = [(3, 0), (1, 3)]
    print solution(matrix, points)
