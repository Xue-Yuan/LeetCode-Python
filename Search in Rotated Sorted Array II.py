class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        b, e = 0, len(nums)-1
        while b <= e:
            m = b + (e-b) / 2
            if target == nums[m]:
                return True
            if nums[m] > nums[e]:
                if nums[b] <= target < nums[m]:
                    e = m-1
                else:
                    b = m+1
            elif nums[m] < nums[e]:
                if nums[m] < target <= nums[e]:
                    b = m+1
                else:
                    e = m-1
            else:
                e -= 1
        return False
