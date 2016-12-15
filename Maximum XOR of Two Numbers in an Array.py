class TrieNode(object):
    def __init__(self):
        self.kids = [None] * 2


def insert(root, num):
    if root is None:
        root = TrieNode()
    node = root
    for bit in map(int, '{:032b}'.format(num)):
        if node.kids[bit] is None:
            node.kids[bit] = TrieNode()
        node = node.kids[bit]
    return root


def query(root, num):
    ans, flipper = 0, 1 << 31
    node = root
    for bit in map(int, '{:032b}'.format(num)):
        if node.kids[bit ^ 0x1]:
            ans |= flipper
            node = node.kids[bit ^ 0x1]
        else:
            node = node.kids[bit]
        flipper >>= 1
    return ans


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        root = insert(None, nums[0])
        ans = 0
        for num in nums[1:]:
            ans = max(ans, query(root, num))
            print(ans)
            root = insert(root, num)
        return ans


"""Problem2: Given an array of integers, find the subarray with maximum XOR.
"""


def solution2(nums):
    ans, trie, xors = 0, TrieNode(), 0
    for num in nums:
        xors ^= num
        ans = max(ans, query(trie, xors))
        insert(trie, xors)
    return ans

