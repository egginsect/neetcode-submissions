class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n]*m
        def recursive(i, j):
            if i==m or j==n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if grid[i][j] > 0:
                return grid[i][j]
            return recursive(i+1, j)+recursive(i, j+1)
        return recursive(0, 0)
        