class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        radius, sz = float('-inf'), len(heaters)
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            if idx == sz:
                radius = max(radius, house-heaters[idx-1])
            elif idx == 0:
                radius = max(radius, heaters[idx]-house)
            else:
                radius = max(radius, min(heaters[idx]-house, house-heaters[idx-1]))
        return radius
