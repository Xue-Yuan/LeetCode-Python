class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = idx = 0
        for num in nums:
            if idx != 0 and num == nums[idx-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt <= 2:
                nums[idx] = num
                idx += 1
        return idx


class Solution2(object):
    def removeDuplicates(self, nums):
        idx = 0
        for num in nums:
            if idx < 2 or num > nums[idx-2]:
                nums[idx] = num
                idx += 1
        return idx
