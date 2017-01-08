class TreeNode(object):
    def __init__(self, val, cnt=0):
        self.val = val
        self.cnt = cnt
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node(val: {}, cnt: {})'.format(self.val, self.cnt)


def insert(root, val):
    if not root:
        return TreeNode(val, 1)
    if val <= root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    root.cnt += 1
    return root


def delete(node, key):
    if not node:
        return None
    node.cnt -= 1
    if node.val > key:
        node.left = delete(node.left, key)
    elif node.val < key:
        node.right = delete(node.right, key)
    else:
        if not node.right:
            return node.left
        right = node.right
        while right.left:
            right = right.left
        node.val = right.val
        node.right = delete(node.right, right.val)
    return node


def findKth(root, k):
    left_cnt = root.left.cnt if root.left else 0
    right_cnt = root.right.cnt if root.right else 0
    if k <= left_cnt:
        return findKth(root.left, k)
    elif left_cnt < k <= root.cnt-right_cnt:
        return root.val
    else:
        return findKth(root.right, k-(root.cnt-right_cnt))


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        if k == 1:
            return map(float, nums)
        ans = []
        root = None
        for idx, num in enumerate(nums):
            root = insert(root, num)
            if idx >= k-1:
                median = findKth(root, k/2+1)
                if k & 0x1 == 0x0:
                    median = (median+findKth(root, k/2)) / 2.0
                ans.append(float(median))
                root = delete(root, nums[idx-k+1])
        return ans
