"""A better implementation should always advance
the iterator after calling next.
"""


class Iterator(object):
    def __init__(self, vec):
        self.itr = iter(vec)
        self.val = 0
        self.used = True

    def hasNext(self):
        if not self.used:
            return True
        try:
            self.val = next(self.itr)
            self.used = False
            return not self.used
        except:
            return False

    def next(self):
        self.used = True
        return self.val


class EvenIterator(object):
    def __init__(self, Iterator):
        self.itr = Iterator
        self.used = True
        self.val = 0

    def hasNext(self):
        if not self.used:
            return True
        while self.itr.hasNext() and self.used:
            self.val = self.itr.next()
            if self.val & 0x1 == 0:
                self.used = False
        return not self.used

    def next(self):
        self.used = True
        return self.val


ei = EvenIterator(Iterator([1,2,3,4,5,6,7,8,9]))
while ei.hasNext():
    print ei.next()
