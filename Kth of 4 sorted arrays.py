import heapq


def kthOfFour(vecs, k):
    """vecs is a list of 4 sorted lists. Find the kth smallest element
    from them.
    """
    vecs.sort(key=len)
    if len(vecs[2]) == 0:
        return vecs[3][k-1]
    if k <= 4:
        pq = [(vec[0], vec, 0) for vec in vecs if vec]
        heapq.heapify(pq)
        for _ in range(k):
            val, vec, idx = heapq.heappop(pq)
            if idx+1 < len(vec):
                heapq.heappush(pq, (vec[idx+1], vec, idx+1))
        return val
    i = min(k/4, len(vecs[0]))
    j = min(k/2-i, len(vecs[1]))
    m = min(3*k/4-i-j, len(vecs[2]))
    n = k - m - j - i
    # print 'i={}, j={}, m={}, n={}, k={}'.format(i, j, m, n, k)
    minVal, maxVal = float('inf'), float('-inf')
    for ith, vec in zip((i, j, m, n), vecs):
        if vec:
            minVal = min(minVal, vec[ith-1])
            maxVal = max(maxVal, vec[ith-1])
    newVecs = []
    for ith, vec in zip((i, j, m, n), vecs):
        if vec:
            if minVal == vec[ith-1]:
                newVecs.append(vec[ith:])
                k -= ith
            elif maxVal == vec[ith-1]:
                newVecs.append(vec[:ith+1])
            else:
                newVecs.append(vec)
        else:
            newVecs.append(vec)
    return kthOfFour(newVecs, k)


if __name__ == "__main__":
    vecs = [
        [1,2,3], [4,5,6], [7,8,9], [10,11,12]
    ]
    for i in range(1, 13):
        print kthOfFour(vecs, i),
    print
    vecs = [
        [1,2,3], [], [2,3,4], [4,5,6]
    ]
    for i in range(1, 10):
        print kthOfFour(vecs, i),
    print
    vecs = [
        [1,2,3], [99, 100, 101], [4,5,6,7,8,9], [11,14,15,16]
    ]
    for i in range(1, sum(len(vec) for vec in vecs)):
        print kthOfFour(vecs, i),
    print
