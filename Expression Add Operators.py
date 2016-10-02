class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def search(num, res, path, prev, ans=[]):
            if not num:
                if res == target:
                    ans.append(path)
                return ans
            for i in range(1, len(num)+1):
                cur, val = num[:i], int(num[:i])
                if len(cur) > 1 and cur[0] == '0':
                    continue
                if path:
                    search(num[i:], res+val, path+'+'+cur, val)
                    search(num[i:], res-val, path+'-'+cur, -val)
                    search(num[i:], res-prev+prev*val, path+'*'+cur, prev*val)
                else:
                    search(num[i:], val, cur, val)
            return ans
        return search(num, 0, '', 0)
