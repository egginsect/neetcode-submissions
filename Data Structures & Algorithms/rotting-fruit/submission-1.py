class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh_fruits = set()
        visited = set()
        buf = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_fruits.add((i, j))
                elif grid[i][j] == 2:
                    buf.append((i,j))
        if len(fresh_fruits) == 0:
            return 0
        step = -1
        while buf:
            step+=1
            for _ in range(len(buf)):
                i, j = buf.pop(0)
                print(i,j)
                if (i,j) in fresh_fruits:
                    fresh_fruits.remove((i, j))
                visited.add((i, j))
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if (0 <= ni < m 
                    and 0 <= nj < n
                    and grid[ni][nj] == 1 
                    and (ni,nj) not in visited):
                        buf.append((ni, nj))
        return step if len(fresh_fruits) == 0 else -1
                