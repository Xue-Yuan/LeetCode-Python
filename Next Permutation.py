class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        sz = len(nums)
        for i in reversed(range(sz)):
            if i > 0 and nums[i-1] < nums[i]:
                for j in reversed(range(sz)):
                    if nums[i-1] < nums[j]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        break
                break
        nums[i:] = nums[i:][::-1]
