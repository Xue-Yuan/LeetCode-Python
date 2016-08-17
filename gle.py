"""
strs = ["cat", "rabbit", "dog", "mouse"]
ints = [2, 0, 3, 1]
change strs to ["dog", "cat", "mouse", "rabbit"]
数字数组 对应 字符串数组 元素变换后的下标
"""


def solution(strs, ints):
    for idx in range(len(ints)):
        val = ints[idx]
        while val >= 0 and ints[val] >= 0 and idx != val:
            strs[val], strs[idx] = strs[idx], strs[val]
            ints[idx] = -1
            idx = val
            val = ints[idx]

strs1 = ["cat", "mouse", "dog", "rabbit", "tiger", "lion"]
ints1 = [2, 0, 1, 3, 5, 4]
"""['dog', 'mouse', 'cat', 'rabbit', 'lion', 'tiger']"""
solution(strs1, ints1)
print strs1
