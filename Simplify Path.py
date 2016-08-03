class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stk, files = [], filter(None, path.split('/'))
        for file in files:
            if file == '..':
                if stk:
                    stk.pop()
            elif file != '.':
                stk.append(file)
        return '/' + '/'.join(stk)
