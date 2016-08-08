m = {
    '1': '',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ret, path = [], []

        def dfs(digits, idx):
            if idx == len(digits):
                ret.append(''.join(path))
            else:
                for ch in m[digits[idx]]:
                    path.append(ch)
                    dfs(digits, idx+1)
                    path.pop()

        if digits != '':
            dfs(digits, 0)
        return ret
