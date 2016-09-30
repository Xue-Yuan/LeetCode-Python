class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            start, end = i+1, len(nums)-1
            while start < end:
                s = nums[i] + nums[start] + nums[end]
                if s < target:
                    ans += end-start
                    start += 1
                else:
                    end -= 1
        return ans
