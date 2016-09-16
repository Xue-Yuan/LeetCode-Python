import collections


class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cntr = collections.Counter(s)
        single = [k for k, v in cntr.items() if v & 0x1]
        if len(single) > 1:
            return []
        half = [k*(v/2) for k, v in cntr.items() if v > 1]
        half.sort()
        return list(self.nextPermutation(half, single))

    def nextPermutation(self, nums, single):
        yield ''.join(nums + single + nums[::-1])
        while True:
            k = -1
            for i in range(len(nums)-1):
                if nums[i] < nums[i+1]:
                    k = i
            if k == -1:
                return
            else:
                l = -1
                for i in range(k+1, len(nums)):
                    if nums[k] < nums[i]:
                        l = i
                nums[k], nums[l] = nums[l], nums[k]
                nums[:] = nums[:k+1] + nums[:k:-1]
                yield ''.join(nums + single + nums[::-1])


if __name__ == '__main__':
    solution = Solution()
    print solution.generatePalindromes('aabb')
    print solution.generatePalindromes('abc')
    print solution.generatePalindromes('aab')
