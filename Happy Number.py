class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = set()
        while n not in record:
            if n == 1:
                return True
            record.add(n)
            n = sum(int(ch)**2 for ch in str(n))
        return False
