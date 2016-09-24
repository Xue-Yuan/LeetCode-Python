class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = range(1, n+1)
        ans = ''
        k -= 1
        while nums:
            total = math.factorial(n-1)
            idx, k = divmod(k, total)
            ans += str(nums.pop(idx))
            n -= 1
        return ans
