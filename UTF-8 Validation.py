class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        idx = 0
        while idx < len(data):
            cnt = '{:08b}'.format(data[idx]).find('0')
            if cnt not in (0, 2, 3, 4):
                return False
            for _ in range(cnt-1):
                idx += 1
                if idx >= len(data) or (0xc0 & data[idx]) != 0x80:
                    return False
            idx += 1
        return True
