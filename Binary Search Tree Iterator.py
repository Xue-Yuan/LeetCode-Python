# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        stk = []
        while root:
            stk.append(root)
            root = root.left
        self.stk = stk

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.stk)

    def next(self):
        """
        :rtype: int
        """
        ret = self.stk.pop()
        tmp = ret.right
        while tmp:
            self.stk.append(tmp)
            tmp = tmp.left
        return ret.val


class BSTIterator2(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.cur = root
        self.stk = []

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.cur:
            self.stk.append(self.cur)
            self.cur = self.cur.left
        return len(self.stk) > 0

    def next(self):
        """
        :rtype: int
        """
        tmp = self.stk.pop()
        self.cur = tmp.right
        return tmp.val
