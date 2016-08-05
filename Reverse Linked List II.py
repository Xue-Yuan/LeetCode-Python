# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pre = ph = ListNode(0)
        pre.next = head
        for _ in range(m-1):
            pre = pre.next
        ps = pre.next
        for _ in range(m, n):
            p = ps.next
            ps.next = p.next
            p.next = pre.next
            pre.next = p
        return ph.next
