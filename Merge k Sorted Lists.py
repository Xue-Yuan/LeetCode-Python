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
        import heapq
        ph = cur = ListNode(0)
        pq = [(n.val, n) for n in lists if n]
        heapq.heapify(pq)
        while len(pq):
            _, n = pq[0]
            if n.next:
                heapq.heapreplace(pq, (n.next.val, n.next))
            else:
                heapq.heappop(pq)
            cur.next = n
            cur = cur.next
        return ph.next
