"""Kosaraju's algorithm for strongly connected components in a directed graph.
"""


def transpose_graph(graph):
    newgraph = [[] for _ in range(len(graph))]
    for cur in range(len(graph)):
        for nxt in graph[cur]:
            newgraph[nxt].append(cur)
    return newgraph


def kosaraju(graph):
    def build_stk(graph, cur, stk, visited=set()):
        if cur in visited:
            return
        visited.add(cur)
        for nxt in graph[cur]:
            build_stk(graph, nxt, stk)
        stk.append(cur)

    stk = []
    for cur in range(len(graph)):
        build_stk(graph, cur, stk)
    t_graph = transpose_graph(graph)

    def dfs_print(cur, graph, visited=set()):
        if cur in visited:
            return
        visited.add(cur)
        print cur,
        for nxt in graph[cur]:
            dfs_print(nxt, graph)

    while stk:
        dfs_print(stk.pop(), t_graph)
        print


if __name__ == "__main__":
    graph = [
        [2, 3],
        [0],
        [1],
        [4],
        [],
    ]
    kosaraju(graph)
