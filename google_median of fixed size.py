class Median(object):
    def __init__(self):
        self.arr = [0] * 2049
        self.total = 0

    def add(self, num):
        self.arr[num] += 1
        self.total += 1

    def get(self):
        def _get_kth(k):
            arr, sum_ = self.arr, 0
            for idx, num in enumerate(arr):
                sum_ += num
                if sum_ >= k:
                    break
            return idx
        mid = (self.total+1) / 2
        if self.total & 0x1:
            return _get_kth(mid)
        else:
            return (_get_kth(mid) + _get_kth(mid+1)) / 2.


median = Median()
median.add(1)
print median.get()
median.add(100)
print median.get()
median.add(50)
print median.get()
median.add(50)
print median.get()
