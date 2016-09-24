# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        cnt, cur = 1, head
        while cur and cur.next:
            cnt += 1
            cur = cur.next
        cur.next = head
        k %= cnt
        for _ in range(cnt-k):
            cur = cur.next
        ans = cur.next
        cur.next = None
        return ans
