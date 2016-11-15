class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        stk, ser = [], []
        while stk or root:
            while root:
                ser.append(str(root.val))
                stk.append(root)
                root = root.left
            root = stk.pop().right
        return ' '.join(ser)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        dummy = TreeNode(float('inf'))
        stk = [dummy]
        for num in map(int, data.split()):
            cur = TreeNode(num)
            if num < stk[-1].val:
                stk[-1].left = cur
                stk.append(cur)
            else:
                while num > stk[-1].val:
                    tmp = stk.pop()
                tmp.right = cur
                stk.append(cur)
        return dummy.left
