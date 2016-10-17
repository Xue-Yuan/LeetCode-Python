class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, beg, ans=[]):
            if beg == len(nums):
                ans.append(nums)
            for idx in range(beg, len(nums)):
                nums[beg], nums[idx] = nums[idx], nums[beg]
                dfs(nums[:], beg+1)
            return ans
        return dfs(nums, 0)


class Solution2(object):
    def permute(self, nums):
        perms = [[]]
        for n in nums:
            perms = [
                p[:i] + [n] + p[i:]
                for p in perms
                for i in range(len(p)+1)
            ]
        return perms
