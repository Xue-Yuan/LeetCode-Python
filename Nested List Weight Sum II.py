# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if not nestedList:
            return 0
        maxDepth = max(self.findDepth(item) for item in nestedList)
        def _dfs(item, depth):
            if item.isInteger():
                return item.getInteger() * depth
            lst = item.getList()
            return sum(_dfs(nxt, depth-1) for nxt in lst) if lst else 0
        return sum(_dfs(item, maxDepth) for item in nestedList)

    def findDepth(self, nestedinteger):
        if nestedinteger.isInteger():
            return 1
        lst = nestedinteger.getList()
        return (1 + max(self.findDepth(item) for item in lst)) if lst else 1


class Solution2(object):
    def depthSumInverse(self, nestedList):
        total = lvl_sum = 0
        while nestedList:
            tmp = []
            for item in nestedList:
                if item.isInteger():
                    lvl_sum += item.getInteger()
                else:
                    tmp += item.getList()
            total += lvl_sum
            nestedList = tmp
        return total
