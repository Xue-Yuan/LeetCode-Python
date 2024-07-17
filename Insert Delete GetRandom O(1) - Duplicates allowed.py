class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = collections.defaultdict(set)
        self.arr = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        m, arr = self.m, self.arr
        m[val].add(len(arr))
        arr.append(val)
        return len(m[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        m, arr = self.m, self.arr
        if val not in m:
            return False
        pos = m[val].pop()
        if not m[val]:
            del m[val]
        if pos != len(arr) - 1:
            arr[pos] = arr[-1]
            m[arr[-1]].add(pos)
            m[arr[-1]].discard(len(arr) - 1)
        arr.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
