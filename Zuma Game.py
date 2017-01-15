class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        def eliminate(cur, idx):
            if not cur:
                return cur
            l, r = idx-1, idx+1
            while l >= 0 and cur[l] == cur[idx]:
                l -= 1
            while r < len(cur) and cur[r] == cur[idx]:
                r += 1
            if r-l-1 >= 3:
                return eliminate(cur[:l+1] + cur[r:], max(0, l))
            return cur

        memo = {}

        def dfs(board, hand, cnt):
            if (board, hand) not in memo:
                if not board:
                    return cnt
                if not hand:
                    return -1
                ans = -1
                for i in range(len(board)):
                    for j in range(len(hand)):
                        if board[i] != hand[j]:
                            continue
                        nxt = eliminate(board[:i] + hand[j] + board[i:], i)
                        tmp = dfs(nxt, hand[:j] + hand[j+1:], cnt+1)
                        if ans < 0:
                            ans = tmp
                        elif tmp > 0:
                            ans = min(ans, tmp)
                memo[board, hand] = ans
            return memo[board, hand]

        return dfs(board, hand, 0)
