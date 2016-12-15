class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.indices = {}
        self.vec = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.indices:
            self.indices[val] = len(self.vec)
            self.vec.append(val)
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.indices:
            return False
        if len(self.vec) == 1 or self.vec[-1] == val:
            self.vec.pop()
            del self.indices[val]
        else:
            idx = self.indices[val]
            self.indices[self.vec[-1]] = idx
            self.vec[idx] = self.vec[-1]
            del self.indices[val]
            self.vec.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.vec)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
