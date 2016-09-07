class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        beg = pre = nums[0]
        ans = []
        for cur in nums[1:] + [nums[-1]]:
            if cur == pre + 1:
                pre = cur
            else:
                if beg == pre:
                    ans.append(str(beg))
                else:
                    ans.append('{0}->{1}'.format(beg, pre))
                beg = pre = cur
        return ans
