class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ret = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                ret = s if abs(s-target) < abs(ret-target) else ret
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s
        return ret
