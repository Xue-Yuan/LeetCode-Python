class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lvl_print(root, lvl):
    front = []
    cur = root
    while lvl >= 0 and cur:
        front.append((cur, lvl))
        cur = cur.left
        lvl -= 1

    def has_next(front):
        while front and front[-1][1] != 0:
            tmp, lvl = front.pop()
            cur = tmp.right
            while cur and lvl-1 >= 0:
                front.append((cur, lvl-1))
                cur = cur.left
                lvl -= 1
        return bool(front)

    while has_next(front):
        yield front.pop()[0].val


def insert(root, val):
    if not root:
        return Node(val)
    if root.val < val:
        root.right = insert(root.right, val)
    elif root.val > val:
        root.left = insert(root.left, val)
    return root


def out(root):
    if not root:
        return
    out(root.left)
    print root.val
    out(root.right)


if __name__ == '__main__':
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 7)
    root = insert(root, 1)
    root = insert(root, 4)
    root = insert(root, 6)
    root = insert(root, 8)
    # alternative(root, 1)
    for val in lvl_print(root, 2):
        print val,
