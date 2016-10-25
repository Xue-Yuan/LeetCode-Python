# coding: utf-8

"""
给一个Double Linked List，例如：
1<=>2<=>3<=>4<=>5
再给一个List，存的是某些Node的指针，例如存的是1,3,4,5，
要求找这些Node里有多少group，一个Group里的Node是连通的
比如3,4,5是连通的，但是不和1直接连通，所以返回2个group

后来在网上看到更详细的描述，这个题只给了部份node，那么可以
用union-find来做
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


class UnionFind(object):
    def __init__(self):
        self.rank = {}
        self.id = {}
        self.cnt = 0

    def add(self, elem):
        self.id[elem] = elem
        self.rank[elem] = 1
        self.cnt += 1

    def find(self, elem):
        if elem != self.id[elem]:
            self.id[elem] = self.find(self.id[elem])
        return self.id[elem]

    def unite(self, p, q):
        i, j = self.find(p), self.find(q)
        if i == j:
            return
        ri, rj = self.rank[i], self.rank[j]
        if ri > rj:
            self.id[j] = i
        elif ri < rj:
            self.id[i] = j
        else:
            self.id[i] = j
            self.rank[j] += 1
        self.cnt -= 1


if __name__ == '__main__':
    lst = LinkedList()
    nodes = []
    nodes.append(lst.append(1))
    lst.append(2)
    nodes.append(lst.append(3))
    nodes.append(lst.append(4))
    nodes.append(lst.append(5))
    print solution(nodes)

    uf = UnionFind()
    for ch in ['A','C','B','E','G','I']:
        if ch not in uf.id:
            uf.add(ch)
        # 改变一下检查相邻的方法
        for neighbor in filter(lambda x: 'A' <= x <= 'Z', (chr(ord(ch)-1), chr(ord(ch)+1))):
            if neighbor in uf.id:
                uf.unite(neighbor, ch)
    print uf.cnt
