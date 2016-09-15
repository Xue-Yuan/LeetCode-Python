class MinHeap:

    def __init__(self, arr):
        self.arr = arr
        for i in reversed(range(len(arr)//2)):
            self._up(i)

    def _up(self, hole):
        sz = len(self.arr)
        tmp = self.arr[hole]
        while hole*2 + 1 < sz:
            child = hole*2 + 1
            if child+1 < sz and self.arr[child+1] < self.arr[child]:
                child += 1
            if tmp > self.arr[child]:
                self.arr[hole] = self.arr[child]
                hole = child
            else:
                break
        self.arr[hole] = tmp

    def _down(self, hole):
        tmp = self.arr[hole]
        while hole > 0:
            parent = (hole-1) >> 1
            if self.arr[parent] > tmp:
                self.arr[hole] = self.arr[parent]
                hole = parent
            else:
                break
        self.arr[hole] = tmp

    def push(self, val):
        self.arr.append(val)
        self._down(len(self.arr)-1)

    def pop(self):
        tmp = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        if self.arr:
            self._up(0)
        return tmp

    def len(self):
        return len(self.arr)

if __name__ == '__main__':
    h = MinHeap([4,3,2,6,1,0,8,7,9,5])
    while h.len():
        print h.pop(),
    print
    h = MinHeap([])
    for item in [4,3,2,6,1,0,8,7,9,5]:
        h.push(item)
        print h.arr
    while h.len():
        print h.pop(),
    print
