class Node(object):
    def __init__(self, start, end, max):
        self.b = start
        self.e = end
        self.max = max
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node(b:{}, e:{}, max:{})'.format(self.b, self.e, self.max)


class SegmentTree(object):
    def __init__(self, nums):
        self.nums = nums
        self.root = self.buildTree(nums, 0, len(nums)-1)

    def buildTree(self, nums, b, e):
        def _buildTree(nums, b, e):
            if b < e:
                m = (b+e) >> 1
                left = _buildTree(nums, b, m)
                right = _buildTree(nums, m+1, e)
                root = Node(b, e, max(left.max, right.max))
                root.left, root.right = left, right
                return root
            elif b == e:
                return Node(b, e, nums[b])
            else:
                return None
        return _buildTree(nums, b, e)

    def query(self, b, e):
        def _query(node, b, e):
            if not node or node.b > e or node.e < b:
                return float('-inf')
            elif b <= node.b and node.e <= e:
                return node.max
            else:
                return max(_query(node.left, b, e), _query(node.right, b, e))
        return _query(self.root, b, e)

    def update(self, idx, val):
        def _update(node, idx, val):
            if not node or not(node.b <= idx <= node.e):
                return float('-inf')
            if node.b == node.e == idx:
                self.nums[idx] = val
                node.max = val
                return val
            l = _update(node.left, idx, val)
            r = _update(node.right, idx, val)
            node.max = max(l, r)
            return node.max
        return _update(self.root, idx, val)


if __name__ == '__main__':
    t = SegmentTree([0,1,2,3,4,5,6,7])
    print t.root
    print t.query(0, 11)
    print t.query(0, 4)
    t.update(7, 11)
    print t.query(0, 11)
