class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        for i in range(0, len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1; r-= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return ret
