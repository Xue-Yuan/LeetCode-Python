def shift_arr(nums, k):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    sz = len(nums)
    for beg in range(gcd(sz, abs(k))):
        cur, val = beg, nums[beg]
        while True:
            nxt = (cur+k) % sz
            nums[nxt], val = val, nums[nxt]
            cur = nxt
            if cur == beg:
                break
    return nums


def shift_arr2(nums, k):
    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    sz = len(nums)
    k = (sz+k) % sz
    reverse(0, sz-1)
    reverse(0, k-1)
    reverse(k, sz-1)
    return nums


if __name__ == "__main__":
    nums = range(4)
    print(shift_arr(nums, 2))
    print(shift_arr2(nums, -2))
