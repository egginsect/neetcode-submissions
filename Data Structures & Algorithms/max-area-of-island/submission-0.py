class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        M = len(grid)
        N = len(grid[0])
        def dfs(i, j):  
            if (min(i, j)<0 or i==M or j==N or grid[i][j] == 0):
                return 0
            count = 1
            grid[i][j] = 0
            count += dfs(i+1, j)
            count += dfs(i-1, j)
            count += dfs(i, j+1)
            count += dfs(i, j-1)
            return count
        for i in range(M):
            for j in range(N):
                max_area = max(dfs(i, j), max_area)
        return max_area