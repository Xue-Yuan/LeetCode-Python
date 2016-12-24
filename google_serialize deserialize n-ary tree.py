class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.kids = []


def serialize(root):
    if not root:
        return ""
    return "{}({})".format(
        root.val,
        ''.join(serialize(kid) for kid in root.kids),
    )


def deserialize(data):
    stk = [TreeNode(0)]
    num = ''
    for ch in data:
        if ch.isdigit():
            num += ch
        elif ch == '(':
            if num:
                tmp = TreeNode(int(num))
                stk[-1].kids.append(tmp)
                stk.append(tmp)
                num = ''
        elif ch == ')':
            stk.pop()
    return stk[-1].kids[0] if data else None


if __name__ == "__main__":
    root = TreeNode(0)
    root.kids = [TreeNode(1), TreeNode(2), TreeNode(3)]
    root.kids[0].kids.append(TreeNode(4))
    root.kids[1].kids = [TreeNode(5), TreeNode(6)]
    data = serialize(root)
    print data
    root = deserialize(data)
    print serialize(root)
