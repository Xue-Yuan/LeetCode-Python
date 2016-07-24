'''https://discuss.leetcode.com/topic/24320/line-reconstruction-by-height

Suppose you have a line of n people in which the k-th person is described by a pair (h,t) , where h is the height of the k-th person and t is the number of people in front of k who have a height greater or equal than h . Write an algorithm to reconstruct the line.

For example, if the line is composed by the following people:

[(7, 0),(4, 4),(7,1), (5, 0), (6,1), (5, 2)]
The original line should be:

[(5,0), (7,0), (5,2), (6,1), (4,4),(7,1)]
'''

'''
It is similar to the problem of leetcode problem 315, Count of smaller
    Numbers After Self.
Think about why we should sort the array in descending order by height,
    then in ascending order by count. What if the count is the number of
    people shorter in front? How should we sort the array then. (Because
    the count means how many people are higher, it would be just convient
    to sort them this way.)
'''


class TreeNode(object):

    def __init__(self, person):
        self.person = person
        self.weight = 1
        self.left = None
        self.right = None


class Soltuion(object):
    '''
    A rope data structure. The weight is just the number of nodes in
        the left sub-tree plus 1 (the root)
    '''
    def line_reconstruction(self, line):
        line.sort(key=lambda x: (-x[0], x[1]))
        root = None
        for person in line:
            root = self.insert(root, person, person[1])
        return list(self.inorder(root))

    def insert(self, root, person, weight):
        if not root:
            return TreeNode(person)
        if root.weight > weight:
            root.weight += 1
            root.left = self.insert(root.left, person, weight)
        else:
            root.right = self.insert(root.right, person, weight-root.weight)
        return root

    def inorder(self, root):
        if not root:
            return
        for person in self.inorder(root.left):
            yield person
        yield root.person
        for person in self.inorder(root.right):
            yield person


if __name__ == 'main':
    line = [(7, 0), (4, 4), (7, 1), (5, 0), (6, 1), (5, 2)]
    s = Soltuion()
    print s.line_reconstruction(line)
