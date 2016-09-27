class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        def _rob(nums):
            take, skip = 0, 0
            for num in nums:
                take, skip = skip + num, max(skip, take)
            return max(take, skip)

        return max(_rob(nums[:-1]), _rob(nums[1:]))
