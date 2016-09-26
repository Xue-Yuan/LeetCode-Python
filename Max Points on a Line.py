# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) < 3:
            return len(points)
        ans = 0
        m = collections.Counter()
        for i1, p1 in enumerate(points):
            same, diff = 1, 0
            for p2 in points[i1+1:]:
                dx, dy = p1.x-p2.x, p1.y-p2.y
                if dx == 0 and dy == 0:
                    same += 1
                else:
                    gcd = self._GCD(dx, dy)
                    dx, dy = dx/gcd, dy/gcd
                    m[dx, dy] += 1
                diff = max(diff, m[dx, dy])
            ans = max(ans, diff+same)
            m.clear()
        return ans

    def _GCD(self, a, b):
        if b == 0:
            return a
        return self._GCD(b, a % b)
