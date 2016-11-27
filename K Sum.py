class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        # write your code here
        sz = len(A)
        opt = [[[0] * (target+1) for _ in range(k+1)] for _ in range(sz+1)]
        for r in range(sz+1):
            opt[r][0][0] = 1
        for i in range(1, sz+1):
            for j in range(1, k+1):
                for t in range(1, target+1):
                    opt[i][j][t] = opt[i-1][j][t]
                    if t >= A[i-1]:
                        opt[i][j][t] += opt[i-1][j-1][t-A[i-1]]
        return opt[sz][k][target]
