class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        l, h = 0, len(nums)
        while l < h:
            mid = (l + h) >> 1
            if mid + 1 == len(nums) or nums[mid] > nums[mid + 1]:
                h = mid
            else:
                l = mid + 1
        return l
