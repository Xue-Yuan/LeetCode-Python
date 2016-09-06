class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = [['', 1]]
        num = ''
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stk.append(['', int(num)])
                num = ''
            else:
                if ch == ']':
                    seq, cnt = stk.pop()
                    stk[-1][0] += seq * cnt
                else:
                    stk[-1][0] += ch
        return stk[-1][0]
