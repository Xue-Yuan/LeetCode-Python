class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        ans = []
        for idx, ch in enumerate(input):
            if ch in op:
                for left in self.diffWaysToCompute(input[:idx]):
                    for right in self.diffWaysToCompute(input[idx+1:]):
                        ans.append(op[ch](left, right))
        return ans or [int(input)]
