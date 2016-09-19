# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def _dfs(ni, lvl):
            if ni.isInteger():
                return ni.getInteger()*lvl
            return sum(_dfs(nxt, lvl+1) for nxt in ni.getList())
        return sum(_dfs(ni, 1) for ni in nestedList)


# DFS. Expand all the children at once, instead of keep it as an iterator.
class Solution2(object):
    def depthSum(self, nestedList):
        stk = [(ni, 1) for ni in nestedList]
        s = 0
        while stk:
            cur, lvl = stk.pop()
            if cur.isInteger():
                s += cur.getInteger() * lvl
            else:
                stk += [(nxt, lvl+1) for nxt in cur.getList()]
        return s
