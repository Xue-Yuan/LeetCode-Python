# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def _(head, tail):
            if head == tail:
                return None
            fast = slow = head
            while fast != tail and fast.next != tail:
                fast = fast.next.next
                slow = slow.next
            root = TreeNode(slow.val)
            root.left = _(head, slow)
            root.right = _(slow.next, tail)
            return root
        return _(head, None)
