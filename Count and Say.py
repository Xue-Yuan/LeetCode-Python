class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = '1'
        for _ in range(n-1):
            pre, cnt, tmp = '', 0, ''
            for ch in ans+' ':
                if ch != pre:
                    if cnt:
                        tmp += str(cnt) + pre
                    pre, cnt = ch, 1
                else:
                    cnt += 1
            ans = tmp
        return ans
