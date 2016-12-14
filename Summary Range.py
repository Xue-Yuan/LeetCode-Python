class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        beg, expected = nums[0], nums[0]+1
        ans = []
        for num in nums[1:] + [nums[0]]:
            if num != expected:
                if beg + 1 != expected:
                    ans.append('{}->{}'.format(beg, expected-1))
                else:
                    ans.append(str(beg))
                beg = num
            expected = num+1
        return ans
