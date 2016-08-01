class Solution(object):
    """Accumulate layer up.
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
    """Accumulate at each bar
    """
    def trap(self, height):
        idxl, idxr = 0, len(height)-1
        maxl, maxr = 0, 0
        ret = 0
        while idxl < idxr:
            if height[idxl] <= height[idxr]:
                if height[idxl] >= maxl:
                    maxl = height[idxl]
                else:
                    ret += maxl - height[idxl]
                idxl += 1
            else:
                if height[idxr] >= maxr:
                    maxr = height[idxr]
                else:
                    ret += maxr - height[idxr]
                idxr -= 1
        return ret
