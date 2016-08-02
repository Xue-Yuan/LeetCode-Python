class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        idx = cur = 0
        while idx <= cur:
            if cur >= len(nums)-1:
                return True
            cur = max(cur, nums[idx]+idx)
            idx += 1
        return False
