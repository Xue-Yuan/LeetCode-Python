class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        opt, ret = list(nums), nums[0]
        for idx in range(1, len(nums)):
            opt[idx] = max(nums[idx], nums[idx] + opt[idx-1])
            ret = max(ret, opt[idx])
        return ret
