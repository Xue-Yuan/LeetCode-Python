#Navie O(n^2) solution. TLE
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        lx = ly = float('inf')
        rx = ry = float('-inf')
        total = 0
        for a, b, c, d in rectangles:
            total += (c-a)*(d-b)
            lx = min(lx, a)
            ly = min(ly, b)
            rx = max(rx, c)
            ry = max(ry, d)

        def is_intersected(r1, r2):
            return not (
                r1[2] <= r2[0] or
                r1[0] >= r2[2] or
                r1[3] <= r2[1] or
                r1[1] >= r2[3]
            )

        sz = len(rectangles)
        for i in range(sz):
            for j in range(i+1, sz):
                if is_intersected(rectangles[i], rectangles[j]):
                    return False
        return total == (rx-lx)*(ry-ly)
