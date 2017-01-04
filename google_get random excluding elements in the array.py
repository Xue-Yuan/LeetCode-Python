import random


def rand():
    return random.uniform(0, 1)


def getWeight(vec, idx):
    return vec[idx] - vec[0] - idx


def getRandom(vec):
    totalWeight = getWeight(vec, len(vec)-1)
    randWeight = int(rand() * (totalWeight-1)) + 1

    def search(b, e, target):
        while b < e:
            m = (b+e) >> 1
            if target >= getWeight(vec, m):
                b = m+1
            else:
                e = m
        return b

    idx = search(0, len(vec), randWeight)-1
    return vec[idx] + randWeight - getWeight(vec, idx)


if __name__ == '__main__':
    vec = [0,3,5,8,13]
    for _ in range(10):
        print(getRandom(vec))
