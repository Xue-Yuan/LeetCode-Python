class Solution(object):
    def minTotalDistance(self, grid):
        total = 0
        for grid in grid, zip(*grid):
            xs = []
            for x, row in enumerate(grid):
                xs += [x] * sum(row)
            mid = xs[len(xs)/2]
            total += sum(abs(x - mid) for x in xs)
        return total
