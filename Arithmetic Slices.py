class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = cnt = 0
        for i in range(2, len(A)):
            if 2*A[i-1] == A[i] + A[i-2]:
                cnt += 1 if cnt else 3
            else:
                if cnt:
                    ans += (cnt-2)*(cnt-1)/2
                cnt = 0
        if cnt:
            ans += (cnt-2)*(cnt-1)/2
        return ans
