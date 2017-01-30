class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        sz = len(timeSeries)
        ans = 0
        for i in range(1, sz):
            ans += min(duration, timeSeries[i] - timeSeries[i-1])
        ans += duration
        return ans
