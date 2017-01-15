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
        mapping = {None: None}
        cur = head
        while cur:
            if cur not in mapping:
                mapping[cur] = RandomListNode(cur.label)
            if cur.next not in mapping:
                mapping[cur.next] = RandomListNode(cur.next.label)
            if cur.random not in mapping:
                mapping[cur.random] = RandomListNode(cur.random.label)
            mapping[cur].next = mapping[cur.next]
            mapping[cur].random = mapping[cur.random]
            cur = cur.next
        return mapping[head]
