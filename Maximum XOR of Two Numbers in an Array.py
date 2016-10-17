"""https://threads-iiith.quora.com/Tutorial-on-Trie-and-example-problems
"""


class Node(object):
    def __init__(self):
        self.kids = [None, None]


class Trie(object):
    def __init__(self):
        self.root = Node()
        self.insert(0)

    def insert(self, num):
        node = self.root
        for i in reversed(range(32)):
            bit = (num >> i) & 0x1
            if not node.kids[bit]:
                node.kids[bit] = Node()
            node = node.kids[bit]

    def query(self, num):
        node, ans = self.root, 0
        for i in reversed(range(32)):
            bit = (num >> i) & 0x1
            if not node.kids[bit ^ 0x1]:
                node = node.kids[bit]
            else:
                ans |= (1 << i)
                node = node.kids[bit ^ 0x1]
        return ans


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        ans, trie = 0, Trie()
        for num in nums:
            ans = max(ans, trie.query(num))
            trie.insert(num)
        return ans


"""Problem2: Given an array of integers, find the subarray with maximum XOR.
"""


def solution2(nums):
    ans, trie, xors = 0, Trie(), 0
    for num in nums:
        xors ^= num
        ans = max(ans, trie.query(xors))
        trie.insert(xors)
    return ans

