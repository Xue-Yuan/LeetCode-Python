class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans, base = 0, 1
        while base <= n:
            (left, mid), right = divmod(n / base, 10), n % base
            if mid == 0:
                ans += left * base
            elif mid == 1:
                ans += left * base + right+1
            else:
                ans += (left+1) * base
            base *= 10
        return ans
