from collections import OrderedDict


class Node(object):
    def __init__(self, cnt):
        self.cnt = cnt
        self.dict = OrderedDict()
        self.prev = None
        self.next = None


class List(object):
    def __init__(self):
        self.head = Node(float("NaN"))
        self.tail = Node(float("NaN"))
        self.head.next = self.tail
        self.tail.prev = self.head

    def empty(self):
        return self.head.next == self.tail

    def append(self, node):
        prev = self.tail.prev
        prev.next = node
        node.next = self.tail
        node.prev = prev
        prev.next = node

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insertAfter(self, node, newNode):
        newNode.next = node.next
        newNode.prev = node
        node.next = newNode
        newNode.next.prev = newNode

    def appendLeft(self, node):
        self.insertAfter(self.head, node)

    @property
    def first(self):
        return self.head.next if not self.empty() else None


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.List = List()
        self.map = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        ret = -1
        if key in self.map:
            node = self.map[key]
            ret = node.dict[key]
            del self.map[key]
            del node.dict[key]
            if node.next.cnt == node.cnt+1:
                node.next.dict[key] = ret
                self.map[key] = node.next
            else:
                newNode = Node(node.cnt+1)
                newNode.dict[key] = ret
                self.List.insertAfter(node, newNode)
                self.map[key] = newNode
            if len(node.dict) == 0:
                self.List.remove(node)
        return ret

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if not self.capacity:
            return
        if key in self.map:
            node = self.map[key]
            del self.map[key]
            del node.dict[key]
            if node.next.cnt == node.cnt+1:
                node.next.dict[key] = value
                self.map[key] = node.next
            else:
                newNode = Node(node.cnt+1)
                newNode.dict[key] = value
                self.List.insertAfter(node, newNode)
                self.map[key] = newNode
            if len(node.dict) == 0:
                self.List.remove(node)
        else:
            if len(self.map) >= self.capacity:
                k, _ = self.List.first.dict.popitem(last=False)
                del self.map[k]
                if len(self.List.first.dict) == 0:
                    self.List.remove(self.List.first)
            if not self.List.empty() and self.List.first.cnt == 1:
                self.map[key] = self.List.first
                self.List.first.dict[key] = value
            else:
                newNode = Node(1)
                newNode.dict[key] = value
                self.List.appendLeft(newNode)
                self.map[key] = newNode

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)
