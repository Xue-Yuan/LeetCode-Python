class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vec = []
        self.m = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        m, vec = self.m, self.vec
        if val in m:
            return False
        m[val] = len(vec)
        vec.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        m, vec = self.m, self.vec
        if val not in m:
            return False
        idx = m[val]
        if idx != len(vec)-1:
            vec[idx] = vec[-1]
            m[vec[-1]] = idx
        del m[val]
        vec.pop()
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
