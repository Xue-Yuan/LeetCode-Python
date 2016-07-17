# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 1:
            return head
        tail = head
        for _ in range(k-1):
            tail = tail.next
            if not tail:
                return head
        tail = tail.next
        ph, ph.next, ps = ListNode(0), head, head
        while ps.next != tail:
            p = ps.next
            ps.next = p.next
            p.next = ph.next
            ph.next = p
        ps.next = self.reverseKGroup(tail, k)
        return ph.next
