class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(grid)
        n = len(grid[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))

        while queue:
            i, j = queue.pop(0)
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0 <=ni<m and 0<=nj<n and grid[ni][nj] == INF:
                    grid[ni][nj] = grid[i][j]+1
                    queue.append((ni, nj))

        