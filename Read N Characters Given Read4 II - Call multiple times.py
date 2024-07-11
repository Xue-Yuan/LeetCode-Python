from typing import List

cnt = 0


def read4(buf: List[str]) -> int:
    global cnt
    cnt += 1
    buf[:] = "abcd"
    if cnt == 5:
        return 2
    if cnt > 5:
        return 0
    return 4


class Solution:

    def __init__(self):
        self.save = [''] * 4
        self.end = 0
        self.start = 0

    def read(self, buf: List[str], n: int) -> int:
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while idx < n:
            if self.start == 0:
                self.end = read4(self.save)
            if self.end == 0:
                break
            while idx < n and self.start < self.end:
                buf[idx] = self.save[self.start]
                idx += 1
                self.start += 1
            if self.start == self.end:
                self.start = 0
        return idx


class Solution2:

    def __init__(self):
        self.save = []

    def read(self, buf: List[str], n: int) -> int:
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while idx < n:
            if not self.save:
                self.save = [''] * 4
                num = read4(self.save)
                self.save = self.save[:num]
            if not self.save:
                return idx
            buf[idx] = self.save.pop(0)
            idx += 1
        return idx


if __name__ == "__main__":
    s = Solution()
    cnt = 0
    b1 = [''] * 10
    print(s.read(b1, 10))
    print(b1)
    b1 = [''] * 14
    print(s.read(b1, 14))
    print(b1)

    s2 = Solution2()
    cnt = 0
    b2 = [''] * 10
    print(s2.read(b2, 10))
    print(b2)
    b2 = [''] * 14
    print(s2.read(b2, 14))
    print(b2)
