"""Find all square words in a given word list. The definition of
square words is for a set of length of k words, there are k words
vertically and horizontally read the same. For example,

k=2
ab
ba
k=3
acf
cbg
fgd
"""


def square_words(words, k):
    def dfs(row):
        if row == k:
            return 1
        cnt = 0
        for word in words:
            if word not in visited:
                grid[row] = word
                visited.add(word)
                if all(grid[row][col] == grid[col][row] for col in range(row)):
                    cnt += dfs(row+1)
                visited.discard(word)
        return cnt

    grid = ['' for _ in range(k)]
    visited = set()
    return dfs(0)


if __name__ == '__main__':
    words = ['acf', 'cbg', 'fgd']
    k = 3
    print square_words(words, k)

    words = ['ab', 'ba']
    k = 2
    print square_words(words, k)
