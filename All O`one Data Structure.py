class Node(object):
    def __init__(self, cnt=0):
        self.prev = None
        self.next = None
        self.cnt = cnt
        self.keys = set()


class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(float("NaN"))
        self.tail = Node(float("NaN"))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_node = {}

    def __repr__(self):
        cur = self.head.next
        ret = []
        while cur != self.tail:
            ret.append('{}:{}'.format(cur.cnt, cur.keys))
            cur = cur.next
        return ', '.join(ret)

    def insert_after(self, node, key):
        if node.next.cnt != node.cnt+1:
            new = Node(node.cnt+1)
            new.keys.add(key)
            new.next = node.next
            new.next.prev = new
            new.prev = node
            node.next = new
            return new
        else:
            node.next.keys.add(key)
            return node.next

    def prepend(self, key):
        if self.head.next.cnt == 1:
            self.head.next.keys.add(key)
            return self.head.next
        else:
            ret = self.insert_after(self.head, key)
            ret.cnt = 1
            return ret

    def insert_before(self, node, key):
        if node.prev.cnt != node.cnt-1:
            new = Node(node.cnt-1)
            new.keys.add(key)
            new.prev = node.prev
            new.prev.next = new
            new.next = node
            node.prev = new
            return new
        else:
            node.prev.keys.add(key)
            return node.prev

    def remove(self, node):
        pre, nxt = node.prev, node.next
        pre.next, nxt.prev = nxt, pre
        node.prev = node.next = None

    def is_empty(self):
        return self.head.next == self.tail

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.key_node:
            node = self.key_node[key]
            node.keys.discard(key)
            self.key_node[key] = self.insert_after(node, key)
            if not node.keys:
                self.remove(node)
        else:
            self.key_node[key] = self.prepend(key)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.key_node:
            node = self.key_node[key]
            node.keys.discard(key)
            if node.cnt > 1:
                self.key_node[key] = self.insert_before(node, key)
            else:
                del self.key_node[key]
            if not node.keys:
                self.remove(node)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.is_empty():
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.is_empty():
            return ""
        return next(iter(self.head.next.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
