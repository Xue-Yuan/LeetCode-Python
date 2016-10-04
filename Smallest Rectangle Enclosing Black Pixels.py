class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        x = y = 0
        for row in image:
            x |= int(''.join(row), 2)
        for col in zip(*image):
            y |= int(''.join(col), 2)
        return bin(x).count('1') * bin(y).count('1')


#https://discuss.leetcode.com/topic/29086/clear-binary-search-python
class Solution2(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        def lower_bound(beg, end, compare):
            while beg < end:
                mid = (beg + end) >> 1
                if compare(mid):
                    end = mid
                else:
                    beg = mid+1
            return beg
        row, col = len(image), len(image[0]) if image else 0
        top = lower_bound(0, x, lambda r: '1' in image[r])
        bottom = lower_bound(x, row, lambda r: '1' not in image[r])
        left = lower_bound(0, y, lambda c: '1' in [image[i][c] for i in range(row)])
        right = lower_bound(y, col, lambda c: '1' not in [image[i][c] for i in range(row)])
        return (bottom-top) * (right-left)


if __name__ == '__main__':
    image = [
        ['0', '0', '1', '0'],
        ['0', '1', '1', '0'],
        ['0', '1', '0', '0'],
    ]
    print Solution().minArea(image, 0, 2)
