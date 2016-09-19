class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
        twice_mid = min(points)[0] + max(points)[0]
        s = set(map(tuple, points))
        return all(
            (twice_mid-x, y) in s
            for x, y in points
        )
