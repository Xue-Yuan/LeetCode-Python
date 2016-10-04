class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]
        indices, candidates = [0 for _ in primes], primes[:]
        while len(uglies) < n:
            cur = min(candidates)
            uglies.append(cur)
            for idx, can in enumerate(candidates):
                if cur == can:
                    indices[idx] += 1
                    candidates[idx] = primes[idx] * uglies[indices[idx]]
        return uglies[-1]
