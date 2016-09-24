class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        b, e = 0, len(nums)-1
        while b <= e:
            m = (b+e)/2
            if target == nums[m]:
                return m
            if nums[m] > nums[e]:
                if nums[b] <= target < nums[m]:
                    e = m-1
                else:
                    b = m+1
            else:
                if nums[m] < target <= nums[e]:
                    b = m+1
                else:
                    e = m-1
        return -1
