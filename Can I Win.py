class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        memo = {}
        
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False

        def dfs(choosable, total):
            if (choosable, total) not in memo:
                if total >= desiredTotal or choosable == 0:
                    return False
                for i in range(maxChoosableInteger):
                    if (choosable >> i) & 0x1:
                        if not dfs(choosable & ~(1 << i), total + i + 1):
                            memo[choosable, total] = True
                            break
                else:
                    memo[choosable, total] = False
            return memo[choosable, total]
        choosable = 0
        for i in range(maxChoosableInteger):
            choosable |= (1 << i)
        for i in range(maxChoosableInteger):
            if not dfs(choosable & ~(1 << i), i + 1):
                return True
        return False
