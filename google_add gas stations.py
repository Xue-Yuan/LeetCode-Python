import heapq


class Interval(object):

    def __init__(self, dist):
        self.dist = dist
        self.gasCnt = 0

    def __lt__(self, other):
        return self.gap() > other.gap()

    def gap(self):
        return float(self.dist) / (self.gasCnt + 1)


def solution(intervals, k):
    heapq.heapify(intervals)
    for _ in range(k):
        cur = heapq.heappop(intervals)
        cur.gasCnt += 1
        heapq.heappush(intervals, cur)
    return intervals[0].gap()


if __name__ == '__main__':
    print(solution([Interval(1), Interval(9)], 2))
