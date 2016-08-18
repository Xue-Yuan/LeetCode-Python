# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.used = True
        self.val = 0

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.used:
            self.val = self.iterator.next()
            self.used = False
        return self.val

    def next(self):
        """
        :rtype: int
        """
        if not self.used:
            self.used = True
            return self.val
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return not self.used or self.iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].


class PeekingIterator2(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.used = True
        self.val = 0
        if iterator.hasNext():
            self.val = iterator.next()
            self.used = False

    def peek(self):
        return self.val

    def next(self):
        tmp = self.val
        self.used = True
        if self.iterator.hasNext():
            self.val = self.iterator.next()
            self.used = False
        return tmp

    def hasNext(self):
        return not self.used
