class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        for num in nums:
            if idx == 0 or num != nums[idx-1]:
                nums[idx] = num
                idx += 1
        return idx
