# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = [(h.val, h) for h in lists if h]
        heapq.heapify(h)
        pre = dummy = ListNode(0)
        while h:
            _, cur = heapq.heappop(h)
            pre.next = cur
            pre = pre.next
            if cur.next:
                heapq.heappush(h, (cur.next.val, cur.next))
        return dummy.next
