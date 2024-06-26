import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.cache.move_to_end(key, last=False)
        return val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.size += 1
            if self.size > self.capacity:
                self.cache.popitem()
                self.size -= 1
        self.cache[key] = value
        self.cache.move_to_end(key, last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
