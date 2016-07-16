m = {'1': '',
     '2': 'abc',
     '3': 'def',
     '4': 'ghi',
     '5': 'jkl',
     '6': 'mno',
     '7': 'pqrs',
     '8': 'tuv',
     '9': 'wxyz',
     }

#Still too C-plus-plus-ic 
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ret = []
        if digits != '':
            self.dfs(digits, 0, [], ret)
        return ret
    
    def dfs(self, digits, i, s, ret):
        if i == len(digits):
            ret.append(''.join(s))
            return
        for c in m[digits[i]]:
            s.append(c)
            self.dfs(digits, i+1, s, ret)
            s.pop()


#A Pyhonic solution, from leetcode discussion
# https://discuss.leetcode.com/topic/11783/one-line-python-solution/2
class Solution(object):
    def letterCombinations(self, digits):
        if digits == '':
            return []
        return reduce(lambda acc, digit:
                        [x + y for x in acc for y in m[digit]],
                      digits,
                      [''],
                      )
