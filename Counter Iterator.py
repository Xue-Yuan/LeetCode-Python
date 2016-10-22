#coding: utf-8

"""实现一个iterator, input 是一个array{3, 8, 0, 12, 2, 9}, 希望输出是
{8, 8, 8, 9, 9},   也就是eventh number代表 词频， oddth number 代表词
{3, 8, 12, 0, 2, 9}， 就是3个8， 0个12， 2个9.
"""


class CounterIterator(object):
    def __init__(self, vec):
        self.itr = iter(vec)
        self.times = 0
        self.val = 0

    def next(self):
        self.times -= 1
        return self.val

    def hasNext(self):
        while not self.times:
            try:
                self.times = next(self.itr)
                self.val = next(self.itr)
            except:
                return False
        return bool(self.times)


if __name__ == '__main__':
    citr = CounterIterator([3, 8, 0, 12, 2, 9])
    while citr.hasNext():
        print citr.next()
