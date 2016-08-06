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
        def _sortedListToBST(head, tail):
            if head == tail:
                return None
            fast = slow = head
            while fast.next != tail and fast.next.next != tail:
                fast = fast.next.next
                slow = slow.next
            root = TreeNode(slow.val)
            root.left = _sortedListToBST(head, slow)
            root.right = _sortedListToBST(slow.next, tail)
            return root

        return _sortedListToBST(head, None)
