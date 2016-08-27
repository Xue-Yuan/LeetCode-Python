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
                if ch in ('+', '-'):
                    sign = (1, -1)[ch == '-']
                elif ch == '(':
                    nums.append(ans)
                    signs.append(sign)
                    ans, sign = 0, 1
                elif ch == ')':
                    ans = nums.pop() + signs.pop() * ans
        return ans
