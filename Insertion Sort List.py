# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ph = ListNode(0)
        while head:
            pre = ph
            while pre.next and pre.next.val < head.val:
                pre = pre.next
            tmp = head.next
            head.next = pre.next
            pre.next = head
            head = tmp
        return ph.next
