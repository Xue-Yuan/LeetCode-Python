class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        opt = []
        for num in nums:
            idx = bisect.bisect_left(opt, num)
            if idx == len(opt):
                opt.append(num)
            else:
                opt[idx] = num
        return len(opt)
