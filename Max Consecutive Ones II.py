class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeros = ans = beg = 0
        for end in range(len(nums)):
            zeros += nums[end] == 0
            while zeros > 1:
                zeros -= nums[beg] == 0
                beg += 1
            ans = max(ans, end-beg+1)
        return ans
