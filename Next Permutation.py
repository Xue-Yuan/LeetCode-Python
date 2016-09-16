class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = -1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                k = i
        if k == -1:
            nums[:] = nums[::-1]
        else:
            l = -1
            for i in range(k+1, len(nums)):
                if nums[k] < nums[i]:
                    l = i
            nums[k], nums[l] = nums[l], nums[k]
            nums[:] = nums[:k+1] + nums[:k:-1]
