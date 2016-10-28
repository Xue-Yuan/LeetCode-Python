"""Given a quadtree structure:

struct QuadNode {
    QuadNode(int num_ones = 0) : ones(num_ones) {}
    int ones{ 0 };
    QuadNode* child[4]{ nullptr };
};

1.Please build a quadtree to represent a 0-1 matrix, assume the matrix is
a square and the dimension is power of 2.
Given two such quadtrees with same depth, please write a function to
calculate how many 1s are overlapped.

2. If any pixel is black, the merge result is black. Write a function to
merge two quad tree.
"""


class QuadNode(object):
    def __init__(self, row, col, sz, ones, allZeros=False, allOnes=False):
        self.row = row
        self.col = col
        self.sz = sz
        self.ones = ones
        self.kids = [None] * 4
        self.allZeros = allZeros
        self.allOnes = allOnes


class QuadTree(object):
    def __init__(self, matrix):
        self.root = self.buildTree(matrix, 0, 0, len(matrix))

    def buildTree(self, matrix, row, col, sz):
        if sz == 1:
            return QuadNode(row, col, sz, matrix[row][col],
                            matrix[row][col] == 0,
                            matrix[row][col] == 1)
        node = QuadNode(row, col, sz, 0)
        sz /= 2
        kids_cord = [
            (row, col, sz), (row+sz, col, sz),
            (row, col+sz, sz), (row+sz, col+sz, sz),
        ]
        for i in range(4):
            node.kids[i] = self.buildTree(matrix, *kids_cord[i])
            node.ones += node.kids[i].ones
        if node.ones == 0 or node.ones == sz*sz:
            node.allZeros = node.ones == 0
            node.allOnes = node.ones == sz*sz
            node.kids[i] = [None] * 4
        return node


def deepCopy(t):
    if not t:
        return None
    node = QuadNode(t.row, t.col, t.sz, t.ones, t.allZeros, t.allOnes)
    node.kids = map(deepCopy, t.kids)
    return node


def merge(t1, t2):
    if t1.allZeros and t2.allZeros:
        return QuadNode(t1.row, t1.col, t1.sz, 0, allZeros=True)
    if t1.allOnes or t2.allZeros:
        return deepCopy(t1)
    if t2.allOnes or t1.allZeros:
        return deepCopy(t2)
    node = QuadNode(t1.row, t1.col, t1.sz, 0)
    node.kids = map(merge, t1.kids, t2.kids)
    node.ones = sum(node.kids[i].ones for i in range(4))
    return node


def overlap(t1, t2):
    if t1.allOnes and t2.allOnes:
        return t1.ones
    if t1.allZeros or t2.allZeros:
        return 0
    return sum(map(overlap, t1.kids, t2.kids))


if __name__ == '__main__':
    m1 = [
        [0, 1],
        [1, 1],
    ]
    m2 = [
        [0, 0],
        [1, 1],
    ]
    t1 = QuadTree(m1)
    t2 = QuadTree(m2)
    t3 = merge(t1.root, t2.root)
    print t3.ones
    print overlap(t1.root, t2.root)
