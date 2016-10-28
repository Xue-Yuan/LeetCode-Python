#coding: utf-8


"""白人大哥，输入一组边，根据边，输出一棵树
例子：输入（b,a),(b,g),(f,b),(b,c),(c,e)，构建的树是
                f
                ｜
                b
            /   |   \
          g     a   c
                    \
                    e
输出应该是：（不同的层，前面有不同的空格）
f
b
  c
   e
  g
  a
"""


from collections import defaultdict


def solution(edges):
    indegrees = defaultdict(int)
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        indegrees[u]
        indegrees[v] += 1
    root = [k for k, v in indegrees.items() if v == 0]

    def dfs(u, lvl=0):
        print ' ' * lvl + u
        for v in graph[u]:
            dfs(v, lvl+1)

    map(dfs, root)


if __name__ == '__main__':
    solution([('b','a'),('b','g'),('f','b'),('b','c'),('c','e')])
