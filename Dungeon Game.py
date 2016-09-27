class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not any(dungeon):
            return -1
        row, col = len(dungeon), len(dungeon[0])
        opt = [sys.maxint] * (col+1)
        opt[col-1] = 1
        for r in reversed(range(row)):
            for c in reversed(range(col)):
                opt[c] = max(min(opt[c], opt[c+1]) - dungeon[r][c], 1)
        return opt[0]
