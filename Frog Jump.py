import collections


class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        indices = {stone: idx for idx, stone in enumerate(stones)}
        reachable = collections.defaultdict(set)
        reachable[0].add(0)
        for idx in range(len(stones)-1):
            if idx in reachable:
                for k in reachable[idx]:
                    for jump in (k-1, k, k+1):
                        if jump > 0 and stones[idx] + jump in indices:
                            tmp = indices[stones[idx]+jump]
                            reachable[tmp].add(jump)
        return len(stones)-1 in reachable


if __name__ == '__main__':
    solution = Solution()
    print solution.canCross([0,1,3,4,5,7,9,10,12])
    print solution.canCross([0,1,2,3,4,8,9,11])
    print solution.canCross([])
    print solution.canCross([0])
    print solution.canCross([0,1,3,5,6,8,12,17])
