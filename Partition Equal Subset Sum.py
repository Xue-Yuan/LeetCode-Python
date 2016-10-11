class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target, sz = sum(nums), len(nums)
        if target & 0x1:
            return False
        target /= 2
        opt = [[False] * (target+1) for _ in range(sz+1)]
        opt[0][0] = True
        for i in range(1, sz+1):
            for t in range(target+1):
                opt[i][t] = opt[i-1][t] or nums[i-1] == target or t >= nums[i-1] and opt[i][t-nums[i-1]]
        return opt[sz][target]
