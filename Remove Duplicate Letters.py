"""
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        indices = {ch: idx for idx, ch in enumerate(s)}
        stk = []
        for idx, ch in enumerate(s):
            if ch not in stk:
                while stk and indices[stk[-1]] > idx and stk[-1] > ch:
                    stk.pop()
                stk.append(ch)
        return ''.join(stk)


if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicateLetters('bcabc')
    print s.removeDuplicateLetters('cbacdcbc')
