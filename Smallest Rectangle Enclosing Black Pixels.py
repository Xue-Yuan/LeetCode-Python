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


if __name__ == '__main__':
    image = [
        ['0', '0', '1', '0'],
        ['0', '1', '1', '0'],
        ['0', '1', '0', '0'],
    ]
    print Solution().minArea(image, 0, 2)
