class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        beg, ans = 0, len(nums)+1
        for idx, num in enumerate(nums):
            s -= num
            while s <= 0:
                ans = min(ans, idx-beg+1)
                s += nums[beg]
                beg += 1
        return ans if ans != len(nums)+1 else 0
