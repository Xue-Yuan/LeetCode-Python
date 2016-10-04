class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        while len(ans) <= num:
            ans += [i + 1 for i in ans]
        return ans[:num+1]
