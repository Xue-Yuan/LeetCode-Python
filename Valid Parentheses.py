class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = {')': '(', ']': '[', '}': '{'}
        stk = []
        for ch in s:
            if stk and ch in m and stk[-1] == m[ch]:
                stk.pop()
            else:
                stk.append(ch)
        return not stk
