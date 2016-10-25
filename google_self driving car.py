"""Simple self-driving car: let a list of instructions is given(aaararaa)
for every second, calculate the destination of the car after car  follows
all instructions. Here 'a' represents accelerate and 'r' represents reverse.
The car is only running along a straight line started at origin=0 and with
velocity v=1. After an instruction 'a', the car will double its velocity.
After  an instruction 'r', the car will reverse direction and reset its its
speed to 1.

Follow up: given a destination(e.g., x= 5 or -5), generate a list of
instructions to make the car arrive at the given destination after
following all instructions. If there are more than one solution, return
the one with minimal length.
"""


import collections


def solution(instructions):
    v, dest = 1, 0
    for idx, ins in enumerate(instructions):
        dest += v
        if ins == 'a':
            v <<= 1
        elif ins == 'r':
            v = -1
    return dest


def followup(x):
    """BFS
    """
    visited = set((1, 0))
    q = collections.deque((1, 0))
    cnt = 0
    while True:
        sz = len(q)
        for _ in range(sz):
            v, p = q.popleft()
            if p == x:
                return cnt
            for nv, np in ((-1, p+v), (v*2, p+v)):
                if (nv, np) not in visited:
                    q.append((nv, np))
                    visited.add(nv, np)
        cnt += 1
