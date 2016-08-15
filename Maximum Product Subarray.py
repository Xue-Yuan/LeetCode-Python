class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        opt_max = opt_min = 1
        ans = nums[0]
        for num in nums:
            tmp1, tmp2 = opt_min*num, opt_max*num
            opt_max, opt_min = max(tmp1, tmp2, num), min(tmp1, tmp2, num)
            ans = max(ans, opt_max)
        return ans
