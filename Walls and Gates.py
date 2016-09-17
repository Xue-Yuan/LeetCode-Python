class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row, col = len(rooms), len(rooms[0]) if rooms else 0
        q = collections.deque([
            (r, c) for r in range(row)
            for c in range(col)
            if rooms[r][c] == 0])
        while q:
            r, c = q.popleft()
            for d_r, d_c in delta:
                new_r, new_c = r+d_r, c+d_c
                if 0 <= new_r < row and 0 <= new_c < col and rooms[new_r][new_c] == (1<<31)-1:
                    q.append((new_r, new_c))
                    rooms[new_r][new_c] = rooms[r][c] + 1
