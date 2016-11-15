class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def alternative(root):
    def front(root):
        if not root:
            return
        for node in front(root.left):
            yield node
        if not root.left and not root.right:
            yield root
        for node in front(root.right):
            yield node

    def back(root):
        if not root:
            return
        for node in back(root.right):
            yield node
        if not root.left and not root.right:
            yield root
        for node in back(root.left):
            yield node

    f, b = front(root), back(root)
    while True:
        one = next(f)
        two = next(b)
        if one.val > two.val:
            break
        print one.val
        print two.val


def alternative2(root):
    front, back = [], []
    cur = root
    while cur:
        front.append(cur)
        cur = cur.left
    cur = root
    while cur:
        back.append(cur)
        cur = cur.right

    def front_next(front):
        while True:
            tmp = front.pop()
            cur = tmp.right
            while cur:
                front.append(cur)
                cur = cur.left
            if not tmp.left and not tmp.right:
                break
        return tmp

    def back_next(back):
        while True:
            tmp = back.pop()
            cur = tmp.left
            while cur:
                back.append(cur)
                cur = cur.right
            if not tmp.left and not tmp.right:
                break
        return tmp

    while True:
        one = front_next(front)
        two = back_next(back)
        if one.val > two.val:
            break
        print one.val
        print two.val


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
    alternative(root)
    alternative2(root)
