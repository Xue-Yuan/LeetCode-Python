from typing import List


class Solution:

    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        for _ in range(volume):
            found = k
            for direction in -1, 1:
                cur = k
                while (0 <= cur + direction < len(heights)
                       and heights[cur + direction] <= heights[cur]):
                    if heights[cur + direction] < heights[cur]:
                        found = cur + direction
                    cur += direction
                if found != k:
                    # Found a position
                    break
            heights[found] += 1
        return heights


if __name__ == '__main__':
    s = Solution()
    print(s.pourWater([2, 1, 1, 2, 1, 2, 2], 4, 3))
    print(s.pourWater([1, 2, 3, 4], 2, 2))
    print(s.pourWater([3, 1, 3], 5, 1))
