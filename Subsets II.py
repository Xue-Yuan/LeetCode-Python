class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret, path = [], []

        def dfs(nums, beg):
            ret.append(path[:])
            for idx in range(beg, len(nums)):
                if beg == idx or nums[idx] != nums[idx-1]:
                    path.append(nums[idx])
                    dfs(nums, idx+1)
                    path.pop()

        dfs(nums, 0)
        return ret
