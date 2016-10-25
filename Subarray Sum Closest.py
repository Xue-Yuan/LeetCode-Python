class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        prefix = [(0, -1)]
        for idx, num in enumerate(nums):
            prefix.append((prefix[-1][0]+num, idx))
        prefix.sort()
        closest = float('inf')
        ans = []
        for i in range(len(prefix)-1):
            if prefix[i+1][0]-prefix[i][0] <= closest:
                closest = prefix[i+1][0]-prefix[i][0]
                ans = [min(prefix[i+1][1], prefix[i][1])+1,
                    max(prefix[i+1][1], prefix[i][1])]
        return sorted(ans)
