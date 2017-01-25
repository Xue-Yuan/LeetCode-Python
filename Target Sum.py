class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        memo = {}
        
        def dfs(beg, target):
            if beg == len(nums):
                if target == S:
                    return 1
                return 0
            if (beg, target) not in memo:
                memo[beg, target] = dfs(beg+1, target-nums[beg]) + dfs(beg+1, target+nums[beg])
            return memo[beg, target]
        return dfs(0, 0)
