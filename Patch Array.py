class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        cnt, missing = 0, 1
        for num in nums:
            while missing < num and missing <= n:
                cnt += 1
                missing <<= 1
            missing += num
        while missing <= n:
            missing <<= 1
            cnt += 1
        return cnt
