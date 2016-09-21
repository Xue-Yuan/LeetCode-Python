#essentially the same problem as the Largest Rectangel in Histogram and Maximal Rectangel

class Solution(object):
    """Accumulate layer up. Take a look at the problem
        Largest Rectangle in Histogram
    """
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stk, ret, idx = [], 0, 0
        while idx < len(height):
            if not stk or height[idx] <= height[stk[-1]]:
                stk.append(idx)
                idx += 1
            else:
                bot = stk.pop()
                if stk:
                    ret += (min(height[stk[-1]], height[idx]) - height[bot]) * (idx - stk[-1] - 1)
        return ret


class Solution2(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        sz = len(height)
        left, right = [height[0]] + [0]*(sz-1), [0]*(sz-1) + [height[-1]]
        for i in range(1, sz):
            left[i] = max(height[i], left[i-1])
            right[~i] = max(height[~i], right[~i+1])
        ans = 0
        for i, h in enumerate(height):
            if h < min(left[i], right[i]):
                ans += min(left[i], right[i]) - h
        return ans


class Solution3(object):
    def trap(self, height):
        """The same idea as Solution2, but slickly combine the two loops.
        """
        l, r = 0, len(height)-1
        ans = maxl = maxr = 0
        while l < r:
            maxl = max(maxl, height[l])
            maxr = max(maxr, height[r])
            if maxl < maxr:
                ans += maxl - height[l]
                l += 1
            else:
                ans += maxr - height[r]
                r -= 1
        return ans

