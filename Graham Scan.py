class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < self.x
        return self.y < other.y

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)


def distanceSquare(p0, p1):
    return (p0.x-p1.x)**2 + (p0.y-p1.y)**2


def oritation(p0, p1, p2):
    """(p1-p0) cross product (p2-p0)
    """
    (x1, y1), (x2, y2) = p1 - p0, p2 - p1
    return x1*y2 - x2*y1


def graham(points):
    p0 = min(points)

    def compare(p1, p2):
        """p1 is considered smaller if
        (p1-p0) cross product (p2-p0) is positive
        """
        o = oritation(p0, p1, p2)
        if o == 0:
            return distanceSquare(p1, p0) - distanceSquare(p2, p0)
        return -o

    points.sort(cmp=compare)
    ans = []
    for point in points:
        while len(ans) > 1 and oritation(ans[-2], ans[-1], point) <= 0:
            ans.pop()
        ans.append(point)
    return ans


if __name__ == "__main__":
    points = [
        Point(0, 3),
        Point(1, 1),
        Point(2, 2),
        Point(4, 4),
        Point(0, 0),
        Point(1, 2),
        Point(3, 1),
        Point(3, 3),
    ]
    print graham(points)
