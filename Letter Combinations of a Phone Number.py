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
        def dfs(digits, path, ans=[]):
            if not digits:
                ans.append(path)
                return ans
            for ch in m[digits[0]]:
                dfs(digits[1:], path+ch)
            return ans
        return dfs(digits, '') if digits else []


class Solution2(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        q = [''] if digits else []
        for digit in digits:
            q = [cur+ch for cur in q for ch in m[digit]]
        return q
