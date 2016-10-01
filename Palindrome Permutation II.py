import collections


class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cntr = collections.Counter(s)
        single = [k for k, v in cntr.items() if v & 0x1]
        if len(single) > 1:
            return []
        half = [k * (v/2) for k, v in cntr.items() if v > 1]
        half.sort()
        return list(self.next_permutation(half, single))

    def next_permutation(self, half, single):
        while True:
            yield ''.join(half + single + half[::-1])
            for i in reversed(range(len(half))):
                if i > 0 and half[i-1] < half[i]:
                    for j in reversed(range(len(half))):
                        if half[j] > half[i-1]:
                            half[i-1], half[j] = half[j], half[i-1]
                            break
                    break
            else:
                return
            half[:] = half[:i] + half[i:][::-1]


if __name__ == '__main__':
    solution = Solution()
    print solution.generatePalindromes('aabb')
    print solution.generatePalindromes('abc')
    print solution.generatePalindromes('aab')
