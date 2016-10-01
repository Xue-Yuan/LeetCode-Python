class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stk, cur = [], None
        for node in preorder:
            if not stk or node < stk[-1]:
                if cur and node <= cur:
                    return False
            else:
                while stk and node > stk[-1]:
                    cur = stk.pop()
            stk.append(node)
        return True
