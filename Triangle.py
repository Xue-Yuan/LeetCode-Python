class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        ret = triangle[-1]
        for row in range(len(triangle)-2, -1, -1):
            for col in range(len(triangle[row])):
                ret[col] = min(ret[col], ret[col+1]) + triangle[row][col]
        return ret[0]
