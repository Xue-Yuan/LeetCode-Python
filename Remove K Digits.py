class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stk = []
        for ch in num:
            while k and stk and stk[-1] > ch:
                stk.pop()
                k -= 1
            stk.append(ch)
        return ''.join(stk[:len(stk)-k]).lstrip('0') or '0'
