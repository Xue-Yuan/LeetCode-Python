import collections


def solution(n):
    states = {(0,) * n: 1}
    for i in range(1, n*n+1):
        new_states = collections.defaultdict(int)
        for state, cnt in states.items():
            for j in range(n):
                if j == 0 or state[j-1] > state[j]:
                    new_state = state[:j] + (state[j]+1, ) + state[j+1:]
                    new_states[new_state] += cnt
        states = new_states
    return new_states[(n,) * n]


if __name__ == '__main__':
    print(solution(5))
