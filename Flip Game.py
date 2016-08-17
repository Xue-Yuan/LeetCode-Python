"""
You are playing the following Flip Game with your friend: Given a string
    that contains only these two characters: + and -, you and your friend
    take turns to flip two consecutive "++" into "--". The game ends when
    a person can no longer make a move and therefore the other person will
    be the winner.

Write a function to compute all possible states of the string after one
    valid move.

For example, given s = "++++", after one move, it may become one of the
    following states:

        [
          "--++",
          "+--+",
          "++--"
        ]
        
If there is no valid move, return an empty list [].
"""


class Solution(object):
    def generatePossibleNextMoves(self, s):
        def dfs(s, idx):
            if idx > len(s)-2:
                return
            if s[idx] == '+' and s[idx+1] == '+':
                ans.append(s[:idx]+'--'+s[idx+2:])
            dfs(s, idx+1)

        ans = []
        dfs(s, 0)
        return ans


if __name__ == '__main__':
    s = "+++-+"
    print Solution().generatePossibleNextMoves(s)
