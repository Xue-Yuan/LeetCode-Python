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


class JumpIterator(object):
    def __init__(self, iterator):
        self.iter = iterator

    def next(self):
        val = self.iter.next()
        if self.iter.hasNext():
            self.iter.next()
        return val

    def hasNext(self):
        return self.iter.hasNext()


itr = Iterator([1,2,3,4,5])
jitr = JumpIterator(itr)
while jitr.hasNext():
    print jitr.next()
