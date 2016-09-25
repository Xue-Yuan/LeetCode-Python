# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

#https://discuss.leetcode.com/topic/1106/o-1-space-o-n-complexity-iterative-solution

class Solution(object):
    """Constant space in traversal
    """
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        cur = root
        while cur:
            head = prev = None
            while cur:
                if cur.left:
                    if prev:
                        prev.next = cur.left
                    else:
                        head = cur.left
                    prev = cur.left
                if cur.right:
                    if prev:
                        prev.next = cur.right
                    else:
                        head = cur.right
                    prev = cur.right
                cur = cur.next
            cur = head


class Solution2:
    """Simple level traversal.
    """
    def connect(self, root):
        pre = dummy = TreeLinkNode(0)
        while root:
            while root:
                if root.left:
                    pre.next = root.left
                    pre = pre.next
                if root.right:
                    pre.next = root.right
                    pre = pre.next
                root = root.next
            root = dummy.next
            dummy.next = None
            pre = dummy
