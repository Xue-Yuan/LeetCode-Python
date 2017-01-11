class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [1, 2, 2]
        cnt, num = 2, 1
        while len(ans) < n:
            ans += [num] * ans[cnt]
            cnt += 1
            if num == 1:
                num = 2
            else:
                num = 1
        return sum(one for one in ans[:n] if one == 1)
