class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ans = []
        for num in nums + [upper+1]:
            if num > lower+1:
                ans.append('{}->{}'.format(lower, num-1))
            elif num == lower+1:
                ans.append(str(lower))
            lower = num+1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print solution.findMissingRanges([0, 1, 3, 50, 75], 0, 99)
    print solution.findMissingRanges([], 0, 99)
    print solution.findMissingRanges([0, 1, 3, 50, 75, 120, 130], 5, 99)
