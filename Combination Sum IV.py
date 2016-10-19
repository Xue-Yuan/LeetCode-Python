class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        m = collections.defaultdict(int)
        m[0] = 1

        def dfs(nums, target):
            if target in m:
                return m[target]
            cnt = 0
            for num in nums:
                if num <= target:
                    cnt += dfs(nums, target-num)
            m[target] += cnt
            return cnt

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
