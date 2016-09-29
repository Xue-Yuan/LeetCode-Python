class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = [1]*len(nums), [1]*len(nums)
        for idx in range(1, len(nums)):
            left[idx] = nums[idx-1] * left[idx-1]
            right[~idx] = nums[~idx+1] * right[~idx+1]
        return [l*r for l, r in zip(left, right)]


class Solution2(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sz = len(nums)
        out = [1] * sz
        for i in range(1, sz):
            out[i] = out[i-1] * nums[i-1]
        right = nums[-1]
        for i in reversed(range(sz-1)):
            out[i] *= right
            right *= nums[i]
        return out
