from typing import List


class Solution:

    def findMissingRanges(self, nums: List[int], lower: int,
                          upper: int) -> List[List[int]]:
        ans = []
        expected = lower
        for num in nums:
            if num > expected:
                ans.append([expected, num - 1])
            expected = num + 1
        if expected < upper:
            ans.append([expected, upper])
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMissingRanges([0, 1, 3, 50, 75], 0, 99))
    print(solution.findMissingRanges([], 0, 99))
    print(solution.findMissingRanges([0, 1, 3, 50, 75, 120, 130], 5, 99))
