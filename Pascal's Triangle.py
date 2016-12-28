def solution(n):
    cur = 1
    print cur,
    for i in range(1, n+1):
        cur = cur * (n-i+1) / i
        print cur,
    print


if __name__ == "__main__":
    for i in range(1, 10):
        solution(i)
