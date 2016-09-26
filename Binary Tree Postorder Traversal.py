# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stk, ans = [], []
        while root or stk:
            if root:
                stk.append((root, False))
                root = root.left
            else:
                cur, twice = stk.pop()
                if twice:
                    ans.append(cur.val)
                else:
                    stk.append((cur, True))
                    root = cur.right
        return ans


class Solution2(object):
    def postorderTraversal(self, root):
        pre, stk, ret = None, [], []
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            cur = stk.pop()
            if not cur.right or pre == cur.right:
                ret.append(cur.val)
                pre = cur
            else:
                stk.append(cur)
                root = cur.right
        return ret
