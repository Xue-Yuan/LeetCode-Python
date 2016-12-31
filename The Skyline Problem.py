class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        def get(b, e):
            if b == e:
                return [[buildings[b][0], buildings[b][2]], [buildings[b][1], 0]]
            elif b > e:
                return []
            else:
                m = (b+e) >> 1
                first, second = get(b, m), get(m+1, e)
                return merge(first, second)

        def merge(first, second):
            ans = []
            h1 = h2 = idx1 = idx2 = 0
            while idx1 < len(first) and idx2 < len(second):
                if first[idx1][0] < second[idx2][0]:
                    x, h1 = first[idx1]
                    idx1 += 1
                elif first[idx1][0] > second[idx2][0]:
                    x, h2 = second[idx2]
                    idx2 += 1
                else:
                    (x, h1), (_, h2) = first[idx1], second[idx2]
                    idx1 += 1
                    idx2 += 1
                h = max(h1, h2)
                if not ans or ans[-1][1] != h:
                    ans.append([x, h])
            ans += first[idx1:]
            ans += second[idx2:]
            return ans

        return get(0, len(buildings)-1)
