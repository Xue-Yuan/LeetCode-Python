class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        m = {}
        for idx, num in enumerate(nums):
            if num in m and idx - m[num] <= abs(k):
                return True
            m[num] = idx
        return False
