# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=167726&ctid=274


def single_elimination(poss, matches, num):
    if len(matches) == 2:  # base case
        if num == matches[0]:
            return poss[matches[0]][matches[1]]
        else:
            return poss[matches[1]][matches[0]]
    half = len(matches)/2
    east = matches[:half] if num in matches[:half] else matches[half:]
    west = matches[half:] if num not in matches[half:] else matches[:half]

    # for the half that contains wanted team
    main = single_elimination(poss, east, num)
    # for the half that doesn't contains wanted team
    sub = [single_elimination(poss, west, team) for team in west]

    return sum([p * main * poss[num][t] for p, t in zip(sub, west)])


if __name__ == '__main__':
    matrix2 = [
        [0.0, 0.9],
        [0.1, 0.0]
    ]

    matches2 = [0, 1]

    matrix4 = [
        [0.0, 0.1, 0.2, 0.3],
        [0.9, 0.0, 0.4, 0.5],
        [0.8, 0.6, 0.0, 0.6],
        [0.7, 0.5, 0.4, 0.0],
    ]

    matches4 = [0, 1, 2, 3, ]
    print(single_elimination(matrix2, matches2, 0))
    print(single_elimination(matrix2, matches2, 1))

    print(single_elimination(matrix4, matches4, 0))
    print(single_elimination(matrix4, matches4, 1))
    print(single_elimination(matrix4, matches4, 2))
    print(single_elimination(matrix4, matches4, 3))
