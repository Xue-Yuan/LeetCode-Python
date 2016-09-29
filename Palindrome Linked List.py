# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def _reverse(head):
            pre, cur = None, head
            while cur:
                pre, cur.next, cur = cur, pre, cur.next
            return pre
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = _reverse(slow)
        while head and second:
            if head.val != second.val:
                return False
            head = head.next
            second = second.next
        return True
