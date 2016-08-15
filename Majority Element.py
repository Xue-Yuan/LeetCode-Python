class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        can, size, cnt = 0, len(nums), 0
        for num in nums:
            if cnt == 0:
                can = num
                cnt = 1
            elif can == num:
                cnt += 1
            else:
                cnt -= 1
        return can
