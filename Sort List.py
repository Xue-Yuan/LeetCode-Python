# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second, slow.next = slow.next, None
        l1 = self.sortList(head)
        l2 = self.sortList(second)
        pre = ph = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            pre.next = l1
            l1, pre = l1.next, pre.next
        pre.next = l1 or l2
        return ph.next
