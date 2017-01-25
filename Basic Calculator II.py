class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        from operator import mul, div, add, sub
        m = {'+': add, '-': sub, '*': mul, '/': lambda x, y: x/y if x*y >= 0 else -(abs(x)/abs(y))}
        nums, ops = [], []
        num, op = '0', '+'
        for ch in s+'+':
            if ch.isdigit():
                num += ch
            elif ch != ' ':
                if op in '+-':
                    nums.append(m[op](0, int(num)))
                else:
                    nums[-1] = m[op](nums[-1], int(num))
                num = '0'
                op = ch
        return sum(nums)
