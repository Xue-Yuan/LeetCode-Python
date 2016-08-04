class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        idx0, idx1, idx2 = 0, 0, len(nums)-1
        mid = 1
        while idx1 <= idx2:
            if nums[idx1] < mid:
                nums[idx0], nums[idx1] = nums[idx1], nums[idx0]
                idx0, idx1 = idx0+1, idx1+1
            elif nums[idx1] > mid:
                nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
                idx2 -= 1
            else:
                idx1 += 1
