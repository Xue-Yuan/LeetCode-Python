# Given a screen with a given width, height and supported min/max
# font size, determine the max font a given string can be displayed
# in. Word or character can’t be broken. Imagine a method
# getWidth(char c, int fontSize) and getHeight(int fontSize) are given


def getWidth(ch, fontSize):
    pass


def getHeight(fontSize):
    pass


def getWordWidth(word, fontSize):
    return sum(getWidth(ch) for ch in getWidth(ch, fontSize))


def getWordHeight(word, fontSize):
    return max(getHeight(ch, fontSize) for ch in word)


def check(words, fontSize, totalWidth, totalHeight):
    """return negative number if under-fit, 0 if just fit, positive if over-fit
    """
    curHeight = curWidth = 0
    idx = 0
    while idx < len(words) and curHeight <= totalHeight:
        word = words[idx]
        if getWordWidth(word) + curWidth > totalWidth:
            curWidth = 0
            curHeight += getWordHeight(word, fontSize)
        else:
            curWidth += getWordWidth(word)
            idx += 1
        if curHeight > totalHeight:
            return 1
    return curHeight - totalHeight


def solution(words, totalWidth, totalHeight, maxFont):
    b, e = 0, maxFont+1
    ans = 0
    while b < e:
        m = (b + e) / 2
        if check(words, m, totalWidth, totalHeight) <= 0:
            ans = max(ans, m)
            b = m+1
        else:
            e = m
    return ans
