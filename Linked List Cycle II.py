# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""The fast ptr is twice as fast as the slow ptr. So by the time they meet
for the first time, the fast ptr goes twice as far as the slow ptr.

|<--L-->|
o---o---o--o
       /    \
       \    /
        ----
2(L + M) = L + c*N + M  ==> L = c*N - M

Nah I give up drawing... Think about it yourself. Or just google it.
"""


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        hasCycle = False
        while not hasCycle and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            hasCycle = fast == slow
        if not hasCycle:
            return None
        slow = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow
