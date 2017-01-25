class Solution(object):
    def splitArray(self, nums, m):
        """Time limit exceeded.
        """
        prefix = [0]
        for num in nums:
            prefix.append(num + prefix[-1])

        memo = {}

        def split(i, m):
            if m == 1:
                return prefix[i]
            if (i, m) not in memo:
                if i == m:
                    memo[i, m] = max(nums[:i+1])
                else:
                    memo[i, m] = min(max(split(j, m-1), prefix[i] - prefix[j]) for j in range(m-1, i))
            return memo[i, m]

        return split(len(nums), m)


class Solution2(object):
    def splitArray(self, nums, m):
        def greedy(target):
            cur = 0
            cnt = 1
            for num in nums:
                cur += num
                if cur > target:
                    cur = num
                    cnt += 1
                    if cnt > m:
                        return False
            return True

        beg, end = max(nums), sum(nums)+1
        while beg < end:
            mid = (beg+end) >> 1
            if greedy(mid):
                end = mid
            else:
                beg = mid+1
        return beg
