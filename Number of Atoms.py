import collections
from typing import Dict, Tuple


class Solution:

    def countOfAtoms(self, formula: str) -> str:

        def count(formula: str) -> Dict[str, int]:
            l = len(formula)
            cntr = collections.Counter()
            i = 0
            while i < l:
                cur = ""
                if formula[i].isupper():
                    cur += formula[i]
                    for i in range(i + 1, l):
                        if not formula[i].islower():
                            break
                        cur += formula[i]
                    else:
                        i += 1
                    num, i = self.getNum(formula, i)
                    cntr[cur] += num
                if i < l and formula[i] == "(":
                    j = self.findClosing(formula, i)
                    tmp_cntr = count(formula[i + 1:j])
                    num, i = self.getNum(formula, j + 1)
                    for k, v in tmp_cntr.items():
                        cntr[k] += v * num
            return cntr

        cntr = count(formula)
        res = []
        for k, v in sorted(cntr.items()):
            res.append(k)
            if v > 1:
                res.append(str(v))
        return "".join(res)

    def findClosing(self, formula: str, start: int) -> int:
        cnt = 0
        for i in range(start, len(formula)):
            cnt += formula[i] == "("
            cnt -= formula[i] == ")"
            if cnt == 0:
                return i

    def getNum(self, formula: str, start: int) -> Tuple[int, int]:
        num = 0
        for i in range(start, len(formula)):
            if formula[i].isnumeric():
                num = num * 10 + int(formula[i])
            else:
                return max(num, 1), i
        return max(num, 1), len(formula)


if __name__ == '__main__':
    s = Solution()
    print(s.countOfAtoms("((HHe28Be26He)9)34"))
