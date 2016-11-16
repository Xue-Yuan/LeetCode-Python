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
    def __init__(self, iterator, jump):
        self.iter = iterator
        self.jump = jump
        self.val = next(iterator, None)
        self.used = self.val is None

    def next(self):
        if self.used:
            self.hasNext()
        self.used = True
        return self.val

    def hasNext(self):
        try:
            if self.used:
                for _ in range(self.jump):
                    if self.iter.hasNext():
                        self.val = next(self.iter)
                    else:
                        break
                    self.used = False
            return not self.used
        except:
            return False


if __name__ == "__main__":
    itr = Iterator(range(1,100))
    jitr = JumpIterator(itr, 6)
    while jitr.hasNext():
        print jitr.next()
