HOLE = float('-inf')
INF = float('inf')


def holdWater(bars, limit):
    ans, water = [], 0
    for bar in bars + [float('inf')]:
        if bar > limit:
            if water:
                ans.append(water)
                water = 0
        else:
            water += limit - bar
    return ans


def holdWaterWithHole(bars, limit):
    sz = len(bars)
    lmax, rmax = [0] * sz, [0] * sz
    for i, b in enumerate(bars):
        if b == HOLE:
            lmax[i] = 0
        else:
            lmax[i] = max(lmax[i-1], bars[i]) if i else INF
    for i, b in enumerate(bars[::-1]):
        if b == HOLE:
            rmax[~i] = 0
        else:
            rmax[~i] = max(rmax[~i+1], b) if i else INF
    # print(lmax, rmax)
    water, ans = 0, []
    for i in range(sz):
        if bars[i] != HOLE:
            cur = max(min(limit, lmax[i], rmax[i]) - bars[i], 0)
            if cur == 0:
                if water:
                    ans.append(water)
                    water = 0
            else:
                water += cur
    if water:
        ans.append(water)
    return ans


limit = 9
bars = [4,4,7,4,4,9,12,4,5,3]
print(holdWater(bars, limit))
bars = [HOLE,4,7,4,4,9,12,4,5,3]
print(holdWaterWithHole(bars, limit))
bars = [HOLE,4,7,4,HOLE,9,12,4,5,3]
print(holdWaterWithHole(bars, limit))
bars = [HOLE,4,7,4,HOLE,9,HOLE,4,5,3]
print(holdWaterWithHole(bars, limit))
