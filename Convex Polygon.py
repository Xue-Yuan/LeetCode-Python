class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        sz = len(points)
        orientations = set()
        for i in range(sz):
            p0, p1, p2 = points[i], points[(i+1)%sz], points[(i+2)%sz]
            orientation = (p1[0]-p0[0])*(p2[1]-p1[1]) - (p1[1]-p0[1])*(p2[0]-p1[0])
            orientations.add(orientation>=0)
        return len(orientations) == 1
