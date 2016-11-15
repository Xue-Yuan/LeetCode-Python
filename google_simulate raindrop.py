import random


def simulate_raindrop():
    side_walk = [[i, i+1] for i in range(102)]
    visited = [False] * 102
    side_cnt = rain_cnt = 0
    while side_cnt < 100:
        rain = random.uniform(1, 101)
        rain_cnt += 1
        where = int(rain)
        if rain < where + 0.5:
            side_walk[where][0] = max(side_walk[where][0], rain+0.5)
            side_walk[where-1][1] = min(side_walk[where-1][1], rain-0.5)
        else:
            side_walk[where][1] = min(side_walk[where][1], rain-0.5)
            side_walk[where+1][0] = max(side_walk[where+1][0], rain+0.5)
        for w in (where-1, where, where+1):
            if not visited[w]:
                if side_walk[w][0] >= side_walk[w][1]:
                    side_cnt += 1
                    visited[w] = True
    return rain_cnt


print sum(simulate_raindrop() for i in range(100)) / 100
