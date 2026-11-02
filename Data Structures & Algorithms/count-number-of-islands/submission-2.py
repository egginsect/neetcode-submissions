class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            grid[i][j] = "0"
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for di, dj in directions:
                new_i, new_j = i+di, j+dj
                if 0<=new_i<m and 0<=new_j<n and grid[new_i][new_j] == "1":
                    dfs(new_i, new_j)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1 
                    dfs(i, j)
        return count