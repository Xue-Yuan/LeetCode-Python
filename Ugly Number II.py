class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [1]
        indices, primes = [0] * 3, [2, 3, 5]
        for _ in range(n-1):
            candidates = [ans[indices[i]] * primes[i] for i in range(3)]
            ans.append(min(candidates))
            for i, c in enumerate(candidates):
                if c == ans[-1]:
                    indices[i] += 1
        return ans[-1]
