class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i in range(len(nums)):
            re = target - nums[i]
            if re in m:
                return [m[re], i]
            m[nums[i]] = i
        return []
