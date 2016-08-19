#coding: utf-8
"""
类似于Candy Crush游戏，在一个棋盘里随机填1,2,3,4，例如：
121
314
124
玩家每一次可以把两个相邻的数字交换一下，比如如果把最中间的1和3交换一下，
那么竖过来三个连续的1就可以被消除，要求随机generate这个棋盘
Follow-up：如何保证一个棋盘可以至少走一步
"""
import random


def solution(n):
    board = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if r < 2 and c < 2:
                board[r][c] = random.randint(1, 4)
            else:
                ban = []
                if r >= 2 and board[r-1][c] == board[r-2][c]:
                    ban.append(board[r-1][c])
                if c >= 2 and board[r][c-1] == board[r][c-1]:
                    ban.append(board[r][c-1])
                can = [i for i in range(1, 5) if i not in ban]
                board[r][c] = can[random.randint(0, len(can)-1)]
    return board


if __name__ == '__main__':
    for row in solution(5):
        print row
