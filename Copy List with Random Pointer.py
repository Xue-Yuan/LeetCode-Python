# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        m = {None: None}
        pre = RandomListNode(0)
        cur = pre.next = head
        while cur:
            if cur not in m:
                m[cur] = RandomListNode(cur.label)
            if cur.random not in m:
                m[cur.random] = RandomListNode(cur.random.label)
            pre.next = m[cur]
            pre.next.random = m[cur.random]
            pre, cur = pre.next, cur.next
        return m[head]
