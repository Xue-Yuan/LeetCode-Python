class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = [' ' for _ in range(max(len(a), len(b)))]
        carry = 0
        for idx in range(len(res)):
            sum = carry
            if idx < len(a):
                sum += int(a[~idx])
            if idx < len(b):
                sum += int(b[~idx])
            res[~idx], carry = str(sum % 2), sum / 2
        return '1' + ''.join(res) if carry else ''.join(res)
