import collections


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q = collections.deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        """
        :type val: int
        :rtype: float
        """
        num, q = 0, self.q
        if len(q) == self.size and q:
            num = q.popleft()
        q.append(val)
        self.sum += val - num
        return 1.0 * self.sum / len(q) if q else 0


class MovingAverage2:

    def __init__(self, size: int):
        self.size = size
        self.arr = [0] * size
        self.idx = 0
        self.total = 0
        self.is_full = False

    def next(self, val: int) -> float:
        self.total += val - self.arr[self.idx]
        self.arr[self.idx] = val
        self.idx = (self.idx + 1) % self.size
        self.is_full = self.is_full or self.idx == 0
        if self.is_full:
            return self.total / self.size
        return self.total / (self.idx)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

if __name__ == "__main__":
    m1 = MovingAverage(3)
    m2 = MovingAverage2(3)
    print(m1.next(1))
    print(m2.next(1))
    print(m1.next(10))
    print(m2.next(10))
    print(m1.next(3))
    print(m2.next(3))
    print(m1.next(5))
    print(m2.next(5))
    print(m1.next(8))
    print(m2.next(8))
