# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        ph = ListNode(0)
        ph.next = head
        start, end = ph, head
        while end:
            if end.val != 9:
                start = end
            end = end.next
        start.val += 1
        start = start.next
        while start:
            start.val = 0
            start = start.next
        return ph if ph.val else ph.next
