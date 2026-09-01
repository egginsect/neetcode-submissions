class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        M, N = len(grid), len(grid[0])
        def dfs(row, col):
            count = 0
            if (min(row, col) < 0 
                or row == M or col == N
                or (row, col) in visited 
                or grid[row][col] == 1):
                return 0
            if row == M-1 and col == N-1:
                return 1
            visited.add((row, col))
            count += dfs(row+1, col)
            count += dfs(row-1, col)
            count += dfs(row, col+1)
            count += dfs(row, col-1)
            visited.remove((row, col))
            return count
        return dfs(0, 0)
