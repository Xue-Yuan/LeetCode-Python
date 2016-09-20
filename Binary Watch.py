import itertools


hours = [8, 4, 2, 1]
minutes = [32, 16, 8, 4, 2, 1]


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        for i in range(0, num+1):
            for _h in self.get_time(hours, i, 12):
                for _m in self.get_time(minutes, num-i, 60):
                    ans.append('{:}:{:02}'.format(_h, _m))
        return ans

    def get_time(self, time, n, limit):
        ans = []
        for comb in itertools.combinations(time, n):
            tmp = sum(comb)
            if tmp < limit:
                ans.append(tmp)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print solution.readBinaryWatch(1)
    print solution.readBinaryWatch(3)
