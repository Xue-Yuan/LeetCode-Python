#coding: utf-8
"""给两个key/value pair的list A 和B（都是根据Key排好序的）, 假设A是左边的list,
B是右边的list, 根据A来join这两个list, （如果只有右边有的Key就不要存在结果里面了）。
;他说现在这两个list很大，内存不够，所以给你的是两个Iterator，结果也用iterator，
写next就可以了
"""


class JointIterater(object):
    def __init__(self, itrA, itrB):
        self.itrA = itrA
        self.itrB = itrB
        self.preB = float('-inf')

    def __iter__(self):
        return self

    def next(self):
        itrA, itrB = self.itrA, self.itrB
        valA = next(itrA)
        while True:
            if valA == self.preB:
                return valA
            elif valA < self.preB:
                valA = next(itrA)
            else:
                self.preB = next(itrB)


if __name__ == '__main__':
    itrA = iter(range(1, 10))
    itrB = iter([2,6,10])
    for i in JointIterater(itrA, itrB):
        print i,
