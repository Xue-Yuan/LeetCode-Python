# Definition for binary tree with next pointer.
# class Node(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

#https://discuss.leetcode.com/topic/1106/o-1-space-o-n-complexity-iterative-solution


class Solution(object):
    """Constant space in traversal
    """

    def connect(self, root: "Node") -> "Node":
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

                 1
                / \
               /   \
        cur-> 2 ->  3
             / \
            /   \
 anchor->  4 ->  5
                 ^
                 |
                pre

    """

    def connect(self, root: "Node") -> "Node":
        pre = anchor = Node(0)
        cur = root
        while cur:
            while cur:
                if cur.left:
                    pre.next = cur.left
                    pre = pre.next
                if cur.right:
                    pre.next = cur.right
                    pre = pre.next
                cur = cur.next
            cur = anchor.next
            anchor.next = None
            pre = anchor
        return root
