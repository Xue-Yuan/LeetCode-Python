class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate(beg, end):
            ret = []
            for cur in range(beg, end):
                for left in generate(beg, cur) or [None]:
                    for right in generate(cur+1, end) or [None]:
                        root = TreeNode(cur)
                        root.left, root.right = left, right
                        ret.append(root)
            return ret

        return generate(1, n+1)
