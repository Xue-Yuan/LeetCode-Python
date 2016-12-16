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
        h = [(node.val, node) for node in lists if node]
        heapq.heapify(h)
        pre = dummy = ListNode(0)
        while h:
            _, cur = heapq.heappop(h)
            pre.next = cur
            pre = pre.next
            cur = cur.next
            if cur:
                heapq.heappush(h, (cur.val, cur))
        return dummy.next
