class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = sum(nums[:3])
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                ans = s if abs(s-target) < abs(ans-target) else ans
                l += s < target
                r -= s > target
                if s == target:
                    return s
        return ans
