class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        n = 0
        for code in data:
            if n:
                if (code & 0b11000000) != 0b10000000:
                    return False
                n -= 1
            else:
                binary = '{:08b}'.format(code)
                n = len(binary) - len(binary.lstrip('1'))
                if n not in (0, 2, 3, 4):
                    return False
                n -= n != 0
        return n == 0
