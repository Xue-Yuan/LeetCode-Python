class Node(object):
    def __init__(self, val, coordinate):
        self.val = val
        self.subRegion = [None] * 4
        self.coordinate = coordinate


class Solution(object):
    def __init__(self, row, col):
        self.root = Node(0, (0, 0, row, col))

    def set(self, x, y, val):
        def _set(node, x, y, coordinate, val):
            x1, y1, x2, y2 = coordinate
            if not (x1 <= x <= x2 and y1 <= y <= y2):
                return node
            if not node:
                node = Node(0, coordinate)
            if x1 == x2 == x and y1 == y2 == y:
                node.val = val
                return node if val else None
            midx, midy = (x1+x2) >> 1, (y1+y2) >> 1
            node.subRegion = [
                _set(node.subRegion[0], x, y, (x1, y1, midx, midy), val),
                _set(node.subRegion[1], x, y, (midx+1, y1, x2, midy), val),
                _set(node.subRegion[2], x, y, (x1, midy+1, midx, y2), val),
                _set(node.subRegion[3], x, y, (midx+1, midy+1, x2, y2), val),
            ]
            node.val = sum(kid.val for kid in node.subRegion if kid)
            return node if node.val else None

        self.root = _set(self.root, x, y, self.root.coordinate, val)

    def getSum(self, x, y):
        def _getSum(node, x1, y1, x2, y2):
            if not node:
                return 0
            r1, c1, r2, c2 = node.coordinate
            if r1 > x2 or r2 < x1 or c1 > y2 or c2 < y1:
                return 0
            if r1 <= x1 and x2 <= r2 and c1 <= y1 and y2 <= c2:
                return node.val
            return sum(_getSum(kid, x1, y1, x2, y2) for kid in node.subRegion)
        return _getSum(self.root, 0, 0, x, y)


if __name__ == '__main__':
    s = Solution(10, 10)
    s.set(1, 1, 9)
    print(s.getSum(1, 1))
    s.set(5, 5, 10)
    print(s.getSum(6, 6))
