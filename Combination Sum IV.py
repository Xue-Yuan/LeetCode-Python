class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {0: 1}

        def dfs(nums, target):
            if target not in memo:
                cnt = 0
                for num in nums:
                    if target >= num:
                        cnt += dfs(nums, target - num)
                memo[target] = cnt
            return memo[target]

        return dfs(nums, target)


class Solution2(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        opt = [1] + [0]*target
        for t in range(1, target+1):
            for num in nums:
                if t-num >= 0:
                    opt[t] += opt[t-num]
        return opt[-1]


# Why is solution 3 incorrect?
# Because it ignores the order.
class Solution3(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sz = len(nums)
        opt = [[0] * (sz+1) for _ in range(target+1)]
        opt[0][0] = 1
        for t in range(target+1):
            for i in range(1, sz+1):
                opt[t][i] += opt[t][i-1]
                if t >= nums[i-1]:
                    opt[t][i] += opt[t-nums[i-1]][i]
        return opt[-1][-1]
