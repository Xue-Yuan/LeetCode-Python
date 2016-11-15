class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for idx in range(len(nums)):
            while nums[idx]-1 != idx:
                pos = nums[idx]-1
                if nums[pos]-1 == pos:
                    break
                nums[pos], nums[idx] = nums[idx], nums[pos]
        return [i+1 for i, n in enumerate(nums) if i != n-1]
