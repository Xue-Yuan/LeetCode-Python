class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sz = len(nums)
        for idx in range(sz):
            while nums[idx] != idx+1:
                tmp = nums[idx]
                if 0 <= tmp-1 < sz and tmp-1 != idx and nums[tmp-1] != tmp:
                    nums[idx], nums[tmp-1] = nums[tmp-1], nums[idx]
                else:
                    break
        for i in range(sz):
            if nums[i] != i+1:
                return i+1
        return sz+1
