"""
n is an array of length 4

left:         1                 n[0]                n[0]*n[1]           n[0]*n[1]*n[2]
right:  n[3]*n[2]*n[1]        n[3]*n[2]                n[3]                     1

"""


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        l = len(nums)
        for i in range(l - 1):
            ans.append(ans[-1] * nums[i])

        cur = 1
        for i in range(l - 1, -1, -1):
            ans[i] *= cur
            cur *= nums[i]

        return ans


class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = [1] * len(nums), [1] * len(nums)
        for idx in range(1, len(nums)):
            left[idx] = nums[idx - 1] * left[idx - 1]
            right[~idx] = nums[~idx + 1] * right[~idx + 1]
        return [l * r for l, r in zip(left, right)]


class Solution2(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sz = len(nums)
        out = [1] * sz
        for i in range(1, sz):
            out[i] = out[i - 1] * nums[i - 1]
        right = nums[-1]
        for i in reversed(range(sz - 1)):
            out[i] *= right
            right *= nums[i]
        return out
