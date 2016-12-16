class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums, signs = [], []
        num, sign = '0', 1
        ans = 0
        for ch in s+' ':
            if ch.isdigit():
                num += ch
            else:
                ans += int(num) * sign
                num = '0'
                if ch in '+-':
                    sign = 1 if ch == '+' else -1
                elif ch == '(':
                    nums.append(ans)
                    signs.append(sign)
                    ans, sign = 0, 1
                elif ch == ')':
                    ans = nums.pop() + signs.pop() * ans
        return ans


# Dijkstra's two stack scanning
class Solution2(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operators, operands = [], []

        def compute():
            # print(operands, operators)
            operand2, operand1 = operands.pop(), operands.pop()
            operator = operators.pop()
            if operator == '+':
                operands.append(operand1 + operand2)
            else:
                operands.append(operand1 - operand2)

        num = ''
        for ch in s + ' ':
            if ch.isdigit():
                num += ch
            else:
                if num:
                    operands.append(int(num))
                    num = ''
                if ch == '(':
                    operators.append(ch)
                elif ch in '+-':
                    if operators and operators[-1] in '+-':
                        compute()
                    operators.append(ch)
                elif ch == ')':
                    while operators[-1] != '(':
                        compute()
                    operators.pop()
        while operators:
            compute()
        return operands[-1]
