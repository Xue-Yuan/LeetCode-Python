class Solution(object):
    def countPrimes(self, n):
        isPrime = [True] * n
        i = 2
        while i*i < n:
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = False
            i += 1
        return sum(isPrime[2:])
