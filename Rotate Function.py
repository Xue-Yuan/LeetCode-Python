class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s, n, f = sum(A), len(A), 0
        for idx, num in enumerate(A):
            f += idx*num
        ans = f
        for k in range(1, n):
            f += s - n*A[-k]
            ans = max(ans, f)
        return ans


if __name__ == '__main__':
    A = [4, 3, 2, 6]
    print Solution().maxRotateFunction(A)
