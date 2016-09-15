class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = (map(int, v.split('.')) for v in (version1, version2))
        for x, y in itertools.izip_longest(v1, v2, fillvalue=0):
            if x != y:
                return 1 if x > y else -1
        return 0
