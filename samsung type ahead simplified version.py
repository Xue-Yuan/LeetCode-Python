"""http://www.1point3acres.com/bbs/thread-197686-1-1.html
"""


import collections


class Typeahead(object):
    def __init__(self, names):
        self.names = names
        dic = collections.defaultdict(set)
        for idx, name in enumerate(names):
            for word in name.split():
                dic[word].add(idx)
        self.dic = dic

    def query(self, name):
        dic = self.dic
        ans = reduce(lambda x, y: x & y, (dic[word] for word in name.split()))
        return [self.names[idx] for idx in ans]


if __name__ == '__main__':
    t = Typeahead(['Jack Clark Wang', 'Clark Dan', 'Liang Zhuge'])
    print t.query('Clark')
    print t.query('Jack Wang')
