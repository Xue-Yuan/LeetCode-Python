"""Note in python2.x, the result of integer division is always rounded down.
e.g. 8/(-10) = -2.
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        m = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.div,
        }
        for token in tokens:
            if token in m:
                op2, op1 = stk.pop(), stk.pop()
                stk.append(m[token](op1, op2))
            else:
                stk.append(int(token))
        return stk[-1]
