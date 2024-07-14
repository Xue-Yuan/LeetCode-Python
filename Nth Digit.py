"""
[0, 9] 1 digit each, total 9 digits
[10, 99] 2 digits each, total 90 digits
[100, 999] 3 digits each, total 900 digits
"""


class Solution:

    def findNthDigit(self, n: int) -> int:
        l, h = 1, 9
        bucket_range = 9
        digit_cnt = 1
        while n > bucket_range:
            n -= bucket_range
            l *= 10
            h = h * 10 + 9
            digit_cnt += 1
            bucket_range = (h - l + 1) * digit_cnt
        # 0-based within bucket [l, h]
        ith_number, ith_digit = divmod(n - 1, digit_cnt)
        num = l + ith_number
        return int(str(num)[ith_digit])


if __name__ == '__main__':
    solution = Solution()
    print(solution.findNthDigit(234))
    print(solution.findNthDigit(11))
