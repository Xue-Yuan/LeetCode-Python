# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        pre, cur = None, slow.next
        slow.next = None
        while cur:
            pre, cur.next, cur = cur, pre, cur.next
        head2 = pre

        pre = ListNode(0)
        while head or head2:
            if head:
                pre.next = head
                pre = pre.next
                head = head.next
            if head2:
                pre.next = head2
                pre = pre.next
                head2 = head2.next
