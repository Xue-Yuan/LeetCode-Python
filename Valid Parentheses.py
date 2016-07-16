class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = {')': '(', '}': '{', ']': '[', }
        stk = []
        for c in s:
            if c in ('(', '[', '{'):
                stk.append(c)
            elif len(stk) == 0 or p[c] != stk[-1]:
                return False
            else:
                stk.pop()
        return len(stk) == 0
