class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        from operator import lt, gt
        for i in range(len(nums)-1):
            if (gt, lt)[i & 0x1](nums[i], nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]
