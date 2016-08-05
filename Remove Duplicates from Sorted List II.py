# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ph = ListNode(0)
        while head:
            if not head.next or head.val != head.next.val:
                pre.next = head
                pre = pre.next
                head = head.next
            else:
                tmp = head.next
                while tmp and tmp.val == head.val:
                    tmp = tmp.next
                head = tmp
        pre.next = None
        return ph.next
