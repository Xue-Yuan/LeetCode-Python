class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        incr = []
        for num in nums:
            idx = bisect.bisect_left(incr, num)
            if idx == len(incr):
                incr.append(num)
            else:
                incr[idx] = num
            if len(incr) == 3:
                return True
        return False
