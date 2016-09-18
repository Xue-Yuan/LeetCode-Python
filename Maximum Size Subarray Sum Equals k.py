class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m, s, ans = {0: -1}, 0, 0
        for i, num in enumerate(nums):
            s += num
            if s - k in m:
                ans = max(ans, i-m[s-k])
            if s not in m:
                m[s] = i
        return ans
