class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, beg, path, ret=[]):
            ret.append(path[:])
            for idx in range(beg, len(nums)):
                if beg == idx or nums[idx] != nums[idx-1]:
                    path.append(nums[idx])
                    dfs(nums, idx+1, path)
                    path.pop()
            return ret
        nums.sort()
        return dfs(nums, 0, [])
