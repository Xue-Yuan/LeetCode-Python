class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, m = 0, set(nums)
        while True:
            if i not in m:
                return i
            i += 1


# Contant space
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        for i in range(l):
            while i != nums[i] and nums[i] < l:
                n = nums[i]
                nums[i], nums[n] = nums[n], nums[i]
        for i, n in enumerate(nums):
            if n != i:
                return i
        return l
