class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stk = []
        for file in path.split('/'):
            if file == '..':
                if stk:
                    stk.pop()
            elif file and file != '.':
                stk.append(file)
        return '/' + '/'.join(stk)
