import random


def pick(k, arr):
    reservoir = arr[:k]
    for i in range(k, len(arr)):
        j = random.randint(0, i)
        if j < k:
            reservoir[j] = arr[i]
    return reservoir


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print pick(5, arr)
