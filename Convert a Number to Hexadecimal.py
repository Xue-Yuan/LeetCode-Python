class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ''
        for _ in range(8):
            ans = '{:x}'.format(num & 0xf) + ans
            num >>= 4
        return ans.lstrip('0') or '0'
