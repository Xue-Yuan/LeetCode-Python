class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        beg, end = 0, len(nums)-1
        while beg < end:
            if beg + 1 == end:
                return beg if nums[beg] > nums[end] else end
            mid = (beg + end) >> 1
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            if nums[mid-1] < nums[mid] < nums[mid+1]:
                beg = mid+1
            else:
                end = mid
        return beg
