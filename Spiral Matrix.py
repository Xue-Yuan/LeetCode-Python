class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row, col = len(matrix), len(matrix[0]) if matrix else 0
        top = left = 0
        bot, right = row-1, col-1
        ans = []
        while top <= bot and left <= right:
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top += 1
            for i in range(top, bot+1):
                ans.append(matrix[i][right])
            right -= 1
            if top <= bot:
                for i in range(right, left-1, -1):
                    ans.append(matrix[bot][i])
            bot -= 1
            if left <= right:
                for i in range(bot, top-1, -1):
                    ans.append(matrix[i][left])
            left += 1
        return ans
