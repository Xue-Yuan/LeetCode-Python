class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        base, idx = 9, 1
        while n > base*idx:
            n -= base * idx
            base *= 10
            idx += 1
        q, r = divmod(n-1, idx)
        return int(str(q + 10**(idx-1))[r])


if __name__ == '__main__':
    solution = Solution()
    print solution.findNthDigit(234)
    print solution.findNthDigit(11)
