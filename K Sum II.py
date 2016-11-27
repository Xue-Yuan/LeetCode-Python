class Solution:
    """
    @param A: An integer array.
    @param k: A positive integer (k <= length(A))
    @param target: Integer
    @return a list of lists of integer 
    """
    def kSumII(self, A, k, target):
        # write your code here
        def dfs(target, beg, k, path, ans):
            if k == 0:
                if target == 0:
                    ans.append(path[:])
                return ans
            for idx in range(beg, len(A)):
                if target >= A[idx]:
                    path.append(A[idx])
                    dfs(target-A[idx], idx+1, k-1, path, ans)
                    path.pop()
            return ans
        return dfs(target, 0, k, [], [])
