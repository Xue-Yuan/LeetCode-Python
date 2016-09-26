class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        beg, end = 0, len(nums)-1
        while beg < end:
            if nums[end] > nums[beg]:
                return nums[beg]
            mid = (beg+end) >> 1
            if nums[end] > nums[mid]:
                end = mid
            else:
                beg = mid+1
        return nums[beg]
