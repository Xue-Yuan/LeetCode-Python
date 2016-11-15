class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        if end not in bank:
            return -1
        front, back, cnt = {start}, {end}, 1
        while front:
            tmp = set()
            for gene in front:
                bank.discard(gene)
                for i in range(len(gene)):
                    for mut in 'ACGT':
                        if gene[i] != mut:
                            new = gene[:i] + mut + gene[i+1:]
                            if new in back:
                                return cnt
                            if new in bank:
                                tmp.add(new)
                                bank.discard(new)
            cnt += 1
            front = tmp
            if len(front) > len(back):
                front, back = back, front
        return -1


if __name__ == '__main__':
    start = "AAAAAAAA"
    end = "CCCCCCCC"
    bank = ["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA","CCCCCCCC"]
    print Solution().minMutation(start, end, bank)
