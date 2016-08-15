class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            self._append(node)
            return node.val
        return -1

    def set(self, key, value):
        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            self._append(node)
            node.val = value
        else:
            self.dic[key] = node = Node(key, value)
            self._append(node)
            if len(self.dic) > self.capacity:
                first = self.head.next
                self._remove(first)
                del self.dic[first.key]

    def _remove(self, node):
        pre, nxt = node.prev, node.next
        pre.next, nxt.prev = nxt, pre

    def _append(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node
