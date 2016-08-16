# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre = ph = ListNode(0)
        while head:
            if head.val != val:
                pre.next = head
                pre = pre.next
            head = head.next
        pre.next = None
        return ph.next
