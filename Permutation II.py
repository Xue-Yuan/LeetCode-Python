class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, beg):
            if beg == len(nums):
                yield nums
            for idx in range(beg, len(nums)):
                if idx == beg or nums[idx] != nums[beg]:
                    nums[idx], nums[beg] = nums[beg], nums[idx]
                    for res in dfs(nums[:], beg+1):
                        yield res

        nums.sort()
        return list(dfs(nums, 0))
