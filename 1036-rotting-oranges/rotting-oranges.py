from collections import deque

class Solution:
    def orangesRotting(self, grid):
        m = len(grid)
        n = len(grid[0])

        q = deque()
        fresh = 0

        # Find all rotten and fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        # Four directions
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        minutes = 0

        # BFS
        while q and fresh > 0:
            size = len(q)
            minutes += 1

            for _ in range(size):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < m and
                        0 <= nc < n and
                        grid[nr][nc] == 1):

                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

        if fresh > 0:
            return -1

        return minutes
        