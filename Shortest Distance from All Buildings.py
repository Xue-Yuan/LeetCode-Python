'''You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
'''

from typing import List
import collections
import math


class Solution:

    def shortestDistance(self, grid: List[List[int]]):
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        total = 0  # total building count
        # cnt: how many buildings can reach (x,y)
        #      if there is a column all blockers, then (x,y) cannot reach every building
        cnt = [[0] * n for _ in range(m)]
        dist = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                total += 1
                q.append((i, j))
                d = 0
                vis = set()  # reset for every free-land
                while q:
                    d += 1
                    for _ in range(len(q)):
                        r, c = q.popleft()
                        for a, b in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                            x, y = r + a, c + b
                            if (0 <= x < m and 0 <= y < n and grid[x][y] == 0
                                    and (x, y) not in vis):
                                cnt[x][y] += 1
                                dist[x][y] += d
                                q.append((x, y))
                                vis.add((x, y))
        ans = math.inf
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and cnt[i][j] == total:
                    ans = min(ans, dist[i][j])
        return -1 if ans == math.inf else ans


if __name__ == "__main__":
    s = Solution()
    grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    print(s.shortestDistance(grid))
