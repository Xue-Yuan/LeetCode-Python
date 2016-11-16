"""A simple practice hashtable
"""


class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class SinglyLinkedList(object):
    def __init__(self):
        self.dummy = Node(0, 0)

    def insert(self, key, val):
        first = self.dummy.next
        new = Node(key, val)
        new.next = first
        self.dummy.next = new

    def lookup(self, key):
        pre = self.dummy
        while pre.next:
            if pre.next.key == key:
                return pre.next
            pre = pre.next
        return None

    def isEmpty(self):
        return self.dummy.next is None

    def delete(self, key):
        pre = self.dummy
        while pre.next:
            if pre.next.key == key:
                break
            pre = pre.next
        pre.next = pre.next.next


class HashTable(object):
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.cnt = 0

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, val):
        self.set(key, val)

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        hv = hash(key) % self.capacity
        return self.arr[hv] is not None and self.arr[hv].lookup(key) is not None

    def set(self, key, val):
        hv = hash(key) % self.capacity
        if self.arr[hv] is None:
            self.arr[hv] = SinglyLinkedList()
        find = self.arr[hv].lookup(key)
        if find is not None:
            find.val = val
        else:
            self.arr[hv].insert(key, val)
            self.cnt += 1
            if self.cnt >= self.capacity/2:
                self.rehashing()

    def get(self, key):
        hv = hash(key) % self.capacity
        if self.arr[hv] is None:
            raise KeyError("Key not found")
        find = self.arr[hv].lookup(key)
        if find is None:
            raise KeyError("Key not found")
        return find.val

    def delete(self, key):
        hv = hash(key) % self.capacity
        if self.arr[hv] is None:
            raise KeyError("Key not found")
        self.arr[hv].delete(key)
        if self.cnt < self.capacity/4:
            self.rehashing()

    def rehashing(self):
        pass


if __name__ == '__main__':
    ht = HashTable()
    for i in range(10):
        ht[i] = i*i
    for i in range(10):
        print ht[i]
