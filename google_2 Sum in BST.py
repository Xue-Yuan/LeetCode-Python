"""Given a BST and a number, find the a 2 number combination which
sums up to the target.
"""


def solution(root, target):
    """O(n) time O(log(n)) space if balanced.
    """
    left, right = [], []
    cur = root
    while cur:
        left.append(cur)
        cur = cur.left
    cur = root
    while cur:
        right.append(cur)
        cur = cur.right

    def bigger(left):
        ret = left.pop()
        cur = ret.right
        while cur:
            left.append(cur)
            cur = cur.left
        yield ret.val

    def smaller(right):
        ret = right.pop()
        cur = ret.left
        while cur:
            right.append(cur)
            cur = cur.right
        yield ret.val

    b_itr, s_itr = bigger(left), smaller(right)
    l, r = next(b_itr), next(s_itr)
    while l != r:
        if l+r == target:
            return True
        elif l+r < target:
            l = next(b_itr)
        else:
            r = next(s_itr)
    return False


"""Or do it recursively
"""


def solution1(root, target):
    def bigger(root):
        if not root:
            return
        for val in bigger(root.left):
            yield val
        yield root.val
        for val in bigger(root.right):
            yield val

    def smaller(root):
        if not root:
            return
        for val in smaller(root.right):
            yield val
        yield root.val
        for val in smaller(root.left):
            yield val

    b_itr, s_itr = bigger(root), smaller(root)
    l, r = next(b_itr), next(s_itr)
    while l != r:
        if l+r == target:
            return True
        elif l+r < target:
            l = next(b_itr)
        else:
            r = next(s_itr)
    return False
