import collections


class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        s = set(stones)
        reachable = collections.defaultdict(set)
        reachable[0].add(0)
        for stone in stones:
            if stone in reachable:
                for k in reachable[stone]:
                    for jump in (k-1, k, k+1):
                        if jump > 0 and stone+jump in s:
                            if stone+jump == stones[-1]:
                                return True
                            reachable[stone+jump].add(jump)
        return stones[-1] in reachable


if __name__ == '__main__':
    solution = Solution()
    print solution.canCross([0,1,3,4,5,7,9,10,12])
    print solution.canCross([0,1,2,3,4,8,9,11])
    print solution.canCross([])
    print solution.canCross([0])
    print solution.canCross([0,1,3,5,6,8,12,17])
