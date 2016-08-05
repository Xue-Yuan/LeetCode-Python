# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        pre_le = ph_le = ListNode(0)
        pre_gt = ph_gt = ListNode(0)
        while head:
            if head.val < x:
                pre_le.next = head
                pre_le = pre_le.next
            else:
                pre_gt.next = head
                pre_gt = pre_gt.next
            head = head.next
        pre_le.next = ph_gt.next
        pre_gt.next = None
        return ph_le.next
