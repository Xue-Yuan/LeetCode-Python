"""A parking lot with only one empty spot. Each step we can move a car
out of its place and move it into the empty spot. Given the initial state
which is src and the final state which is dst, find out the least movement
needed to move the parking lot from src to dst.
"""


def solution(src, dst):
    """https://discuss.leetcode.com/topic/67928/rearrange-parking-lot
    """
    s_m = {val: idx for idx, val in enumerate(src)}
    d_m = {val: idx for idx, val in enumerate(dst)}

    def swap_0():
        for idx, (s, d) in enumerate(zip(src, dst)):
            if s != d:
                idx_0 = s_m[0]
                src[idx_0], src[idx] = src[idx], src[idx_0]
                s_m[0] = idx
                s_m[s] = idx_0
                break
        print src, dst

    while src != dst:
        idx_0 = s_m[0]
        tar = dst[idx_0]
        if tar == 0:
            swap_0()
        else:
            idx_tar = s_m[tar]
            src[idx_0], src[idx_tar] = src[idx_tar], src[idx_0]
            s_m[0] = idx_tar
            s_m[tar] = idx_0
            print src, dst


solution([1,2,3,0,4], [0,3,2,1,4])
