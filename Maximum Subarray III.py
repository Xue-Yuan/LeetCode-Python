"""Initially I was stuck at the recurrence formula:

take[i][j] = max(take[i-1][j], not_take[i-1][j-1])+nums[i-1]
not_take[i][j] = max(take[i-1][j], not_take[i-1][j])

    But for non-overlapping, we can still have subarrays lay
adjacent to each other. So the formula should be re-written as:

take[i][j] = max(take[i-1][j], not_take[i][j-1])+nums[i-1]
not_take[i][j] = max(take[i-1][j], not_take[i-1][j])
"""


import sys


class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        sz = len(nums)
        not_take = [[-sys.maxint] * (k+1) for _ in range(sz+1)]
        take = [[-sys.maxint] * (k+1) for _ in range(sz+1)]
        take[0][0] = not_take[0][0] = 0
        for i in range(1, sz+1):
            take[i][0] = not_take[i][0] = 0
            for j in range(1, k+1):
                take[i][j] = max(take[i-1][j], not_take[i][j-1])+nums[i-1]
                not_take[i][j] = max(take[i-1][j], not_take[i-1][j])
        return max(take[sz][k], not_take[sz][k])


if __name__ == '__main__':
    solution = Solution()
    print solution.maxSubArray([-1,-2,-3,-100,-1,-50], 2)
    print solution.maxSubArray([4,2,7,5,1,3,5], 4)
