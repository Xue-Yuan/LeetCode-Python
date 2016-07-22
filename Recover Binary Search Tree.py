class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.first = self.second = self.prev = None
        self._inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
 
    def _inorder(self, cur):
        if not cur:
            return
        self._inorder(cur.left)
        if self.prev and self.prev.val > cur.val:
            if not self.first:
                self.first = self.prev
            self.second = cur
        self.prev = cur
        self._inorder(cur.right)


class Solution2(object):
    def recoverTree(self, root):
        prev = cur = None
        first = second = None
        for cur in self.morris_inorder(root):
            if prev and prev.val > cur.val:
                if not first:
                    first = prev
                second = cur
            prev = cur
        first.val, second.val = second.val, first.val

    def morris_inorder(self, cur):
        while cur:
            if not cur.left:
                yield cur
                cur = cur.right
            else:
                tmp = cur.left
                while tmp.right and tmp.right != cur:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = cur
                    cur = cur.left
                else:
                    yield cur
                    cur = cur.right
                    tmp.right = None
        