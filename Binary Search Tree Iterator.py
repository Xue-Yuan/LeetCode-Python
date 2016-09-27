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
        self.iterator = self.inorder(root)
        self.cur = 0
        self.used = True

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.used:
            return True
        try:
            self.cur = self.iterator.next()
            self.used = False
        except:
            return False
        return True

    def next(self):
        """
        :rtype: int
        """
        if not self.used:
            ret = self.cur
        else:
            ret = self.iterator.next()
        self.used = True
        return ret

    def inorder(self, root):
        if not root:
            return
        for node in self.inorder(root.left):
            yield node
        yield root.val
        for node in self.inorder(root.right):
            yield node


class BSTIterator(object):
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
        self.cur = self.stk.pop()
        ret = self.cur.val
        self.cur = self.cur.right
        return ret
        