class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        visited = {}
        delta = [(0, -1), (-1, 0), (1,0), (0, 1)]
        def dfs(i, j):
            # check condition
            if i<0 or j<0 or i==m or j==n or grid[i][j]=="0":
                return 
            else:
                grid[i][j] = "0"
                for dx, dy in delta:
                    dfs(i+dx, j+dy)
                

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt+=1
                    dfs(i, j)
        return cnt
                