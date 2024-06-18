from typing import List


class Solution:

    def findBuildings(self, heights: List[int]) -> List[int]:
        l = len(heights)
        highest = 0
        ans = []
        for i in range(l):
            if heights[~i] > highest:
                ans.append(l + ~i)
                highest = heights[~i]
        return ans[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.findBuildings([4, 2, 3, 1]))
    print(s.findBuildings([4, 3, 2, 1]))
    print(s.findBuildings([1, 3, 2, 4]))
