class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        row, col = len(A), len(B[0]) if B else 0
        ans = [[0] * col for _ in range(row)]
        for i, row in enumerate(A):
            for k, eA in enumerate(row):
                if eA:
                    for j, eB in enumerate(B[k]):
                        if eB:
                            ans[i][j] += eA * eB
        return ans
