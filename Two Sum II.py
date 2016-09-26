class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        beg, end = 0, len(numbers)-1
        while beg < end:
            s = numbers[beg] + numbers[end]
            if s == target:
                return [beg+1, end+1]
            elif s > target:
                end -= 1
            else:
                beg += 1
        return [-1, -1]
