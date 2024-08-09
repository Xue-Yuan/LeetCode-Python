from typing import List
import itertools
import collections


class UnionFind:

    def __init__(self):
        self.id = {}

    def add(self, p: str):
        if p not in self.id:
            self.id[p] = p

    def unite(self, p: str, q: str) -> None:
        p, q = self.find(p), self.find(q)
        if p == q:
            return
        self.id[p] = q

    def find(self, p: str) -> str:
        if p == self.id[p]:
            return p
        self.id[p] = self.find(self.id[p])
        return self.id[p]


class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        for _, *emails in accounts:
            for e in emails:
                uf.add(e)
            for e1, e2 in itertools.pairwise(emails):
                uf.unite(e1, e2)

        id_to_emails = collections.defaultdict(set)
        id_to_name = {}
        for name, *emails in accounts:
            id = uf.find(emails[0])
            id_to_emails[id] |= set(emails)
            id_to_name[id] = name

        ans = []
        for id, name in id_to_name.items():
            emails = id_to_emails[id]
            ans.append([name] + sorted(emails))
        return ans
