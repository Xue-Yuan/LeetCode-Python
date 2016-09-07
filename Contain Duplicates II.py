class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        m = set()
        for idx, num in enumerate(nums):
            if idx > k:
                m.discard(nums[idx-k-1])
            if num in m:
                return True
            m.add(num)
        return False
