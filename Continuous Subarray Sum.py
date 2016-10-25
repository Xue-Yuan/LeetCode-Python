class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the 
    #                  first number and the index of the last number
    def continuousSubarraySum(self, A):
        # Write your code here
        ans = float('-inf')
        sum = start = 0
        result = []
        for i, x in enumerate(A):
            if sum < 0:
                sum = x
                start = i
            else:
                sum += x
            if sum > ans:
                ans = sum
                result = [start, i]
        return result
