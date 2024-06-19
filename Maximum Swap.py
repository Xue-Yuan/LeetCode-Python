class Solution:

    def maximumSwap(self, num: int) -> int:
        m = [-1] * 10
        s = list(x for x in str(num))
        for i, ch in enumerate(s):
            m[int(ch)] = i

        for i, ch in enumerate(s):
            n = int(ch)
            for larger in range(9, n, -1):
                if m[larger] < 0:
                    continue
                target = m[larger]
                if target > i:
                    s[i], s[target] = s[target], s[i]
                    return int(''.join(s))

        return num
