class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        beg = end = cur = 0
        ans = len(nums) + 1
        while end < len(nums):
            cur += nums[end]
            while cur >= s:
                ans = min(ans, end-beg+1)
                cur -= nums[beg]
                beg += 1
            end += 1
        return ans if ans <= len(nums) else 0
