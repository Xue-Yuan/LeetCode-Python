# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre = ph = ListNode(0)
        ph.next = head
        node = pre
        for _ in range(n):
            node = node.next
        while node.next:
            node = node.next
            pre = pre.next
        pre.next = pre.next.next
        return ph.next
