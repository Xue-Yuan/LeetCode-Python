# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        m = {None: None}

        def dfs(node):
            if node not in m:
                m[node] = UndirectedGraphNode(node.label)
                for neighbor in node.neighbors:
                    m[node].neighbors.append(dfs(neighbor))
            return m[node]

        return dfs(node)
