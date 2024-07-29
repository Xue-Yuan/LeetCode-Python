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


def printWater(heights: List[int], volume: int, k: int) -> None:
    water = [0] * len(heights)
    filled = heights[:]
    for _ in range(volume):
        found = k
        for direction in -1, 1:
            cur = k
            while (0 <= cur + direction < len(filled)
                   and filled[cur + direction] <= filled[cur]):
                if filled[cur + direction] < filled[cur]:
                    found = cur + direction
                cur += direction
            if found != k:
                # Found a position
                break
        filled[found] += 1
        water[found] += 1

    height = max(filled)
    while height:
        layer = ''
        for i in range(len(heights)):
            if filled[i] == height:
                if water[i]:
                    layer += 'w'
                    water[i] -= 1
                else:
                    layer += '+'
                filled[i] -= 1
            else:
                layer += ' '
        print(layer)
        height -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.pourWater([2, 1, 1, 2, 1, 2, 2], 4, 3))
    printWater([2, 1, 1, 2, 1, 2, 2], 4, 3)
    print(s.pourWater([1, 2, 3, 4], 2, 2))
    printWater([1, 2, 3, 4], 2, 2)
    print(s.pourWater([3, 1, 3], 5, 1))
    printWater([3, 1, 3], 5, 1)
