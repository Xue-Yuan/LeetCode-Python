class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, beg):
            if beg == len(nums):
                yield nums
            for idx in range(beg, len(nums)):
                nums[beg], nums[idx] = nums[idx], nums[beg]
                for res in dfs(nums[:], beg+1):
                    yield res
        return list(dfs(nums, 0))


class Solution2(object):
    def permute(self, nums):
        perms = [[]]   
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in xrange(len(perm)+1):   
                    new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
            perms = new_perms
        return perms
