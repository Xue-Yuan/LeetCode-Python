"""
You are playing the following Flip Game with your friend: Given a
    string that contains only these two characters: + and -, you
    and your friend take turns to flip two consecutive "++" into
    "--". The game ends when a person can no longer make a move
    and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can
    guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
    Derive your algorithm's runtime complexity.
"""


class Solution(object):
    def canwin(self, s):
        for idx in range(len(s)-1):
            if s[idx] == '+' and s[idx+1] == '+':
                tmp = s[:idx] + '--' + s[idx+2:]
                if not self.canwin(tmp):
                    return True
        return False
