class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stk, least = [], float('-inf')
        for num in preorder:
            if num < least:
                return False
            while stk and num > stk[-1]:
                least = stk.pop()
            stk.append(num)
        return True
