class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stk = []
        for node in preorder.split(','):
            stk.append(node)
            while len(stk) > 2 and stk[-1] == stk[-2] == '#':
                if stk[-3] == '#':
                    return False
                stk[-3:] = ['#']
        return len(stk) == 1 and stk[0] == '#'


if __name__ == '__main__':
    s = Solution()
    print s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
    print s.isValidSerialization("9,#,#,1")
    print s.isValidSerialization("1,#,#,#,#")
