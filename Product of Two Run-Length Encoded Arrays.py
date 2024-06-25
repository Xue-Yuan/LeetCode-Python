from typing import List


class Solution:

    def findRLEArray(self, encoded1: List[List[int]],
                     encoded2: List[List[int]]) -> List[List[int]]:
        ans = []
        j = 0
        for v1, f1 in encoded1:
            while f1:
                f = min(f1, encoded2[j][1])
                v = v1 * encoded2[j][0]
                if ans and ans[-1][0] == v:
                    ans[-1][1] += f
                else:
                    ans.append([v, f])
                f1 -= f
                encoded2[j][1] -= f
                if encoded2[j][1] == 0:
                    j += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findRLEArray([[1, 3], [2, 3]], [[6, 3], [3, 3]]))
    print(s.findRLEArray([[1, 3], [2, 1], [3, 2]], [[2, 3], [3, 3]]))
