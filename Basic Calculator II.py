from typing import List


class Solution:
    '''
    3          +      2                *  2
    pre_num    op   cur_num
    '''

    def calculate(self, s: str) -> int:
        res = 0
        pre_num = 0
        cur_num = 0
        op = '+'
        for i, ch in enumerate(s):
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            if ch in '+-/*' or i == len(s) - 1:
                if op == '+':
                    res += pre_num
                    pre_num = cur_num
                elif op == '-':
                    res += pre_num
                    pre_num = -cur_num
                elif op == "*":
                    pre_num = pre_num * cur_num
                elif op == '/':
                    pre_num = int(pre_num / cur_num)
                op = ch
                cur_num = 0
        res += pre_num
        return res


class Solution2:

    def calculate(self, s: str) -> int:
        stk = []
        num = 0
        sign = "+"

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in "+-*/":
                self.update(stk, sign, num)
                sign = ch
                num = 0
        self.update(stk, sign, num)
        return sum(stk)

    def update(self, stk: List[int], op: str, num: int) -> None:
        if op == "+":
            stk.append(num)
        elif op == "-":
            stk.append(-num)
        elif op == "/":
            stk[-1] = int(stk[-1] / num)
        elif op == "*":
            stk[-1] = stk[-1] * num
