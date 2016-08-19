# coding: utf-8

"""
给一个Double Linked List，例如：
1<=>2<=>3<=>4<=>5
再给一个List，存的是某些Node的指针，例如存的是1,3,4,5，
要求找这些Node里有多少group，一个Group里的Node是连通的
比如3,4,5是连通的，但是不和1直接连通，所以返回2个group
"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = head = Node(0)
        self.tail = tail = Node(0)
        head.next, tail.prev = tail, head

    def append(self, val):
        node = Node(val)
        node.prev = self.tail.prev
        node.prev.next = node
        node.next = self.tail
        self.tail.prev = node
        return node


def solution(nodes):
    st = set(nodes)

    def dfs(node):
        if not node:
            return
        if node.next in st:
            st.remove(node.next)
            dfs(node.next)

    for node in nodesimp:
        dfs(node)
    return len(st)

if __name__ == '__main__':
    lst = LinkedList()
    nodes = []
    nodes.append(lst.append(1))
    lst.append(2)
    nodes.append(lst.append(3))
    nodes.append(lst.append(4))
    nodes.append(lst.append(5))
    print solution(nodes)
