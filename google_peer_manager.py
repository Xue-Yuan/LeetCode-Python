from collections import defaultdict


class Company(object):
    def __init__(self):
        self.peer_groups = defaultdict(set)
        self.manage = defaultdict(set)

    def manager(self, m, e):
        pg = self.peer_groups
        if e not in pg:
            pg[e].add(e)
        self.manage[m] = pg[e]

    def isManager(self, m, e):
        if e in self.manage[m]:
            return True
        for sub_m in self.manage[m]:
            if self.isManager(sub_m, e):
                return True
        return False

    def peer(self, a, b):
        pg = self.peer_groups
        if a in pg and b in pg and pg[a] is not pg[b]:
            return False
        if a in pg:
            pg[a].add(b)
            pg[b] = pg[a]
        else:
            pg[b].add(b)
            pg[b].add(a)
            pg[a] = pg[b]
        return True


if __name__ == "__main__":
    c = Company()
    c.peer('Tim', 'Bill')
    c.peer('Bill', 'Mike')
    c.manager('Lucy', 'Tim')
    print c.isManager('Lucy', 'Tim')
    print c.isManager('Lucy', 'Mike')
    c.manager('Amy', 'Lucy')
    print c.isManager('Amy', 'Bill')
