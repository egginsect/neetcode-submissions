from functools import cache
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        out = []
        pacific = set()
        atlantic = set()
        pacific_start = [(i, 0) for i in range(m)]+[(0, j) for j in range(n)]
        atlantic_start = [(i, n-1) for i in range(m)]+[(m-1, j) for j in range(n)]
        
        def bfs(queue, ocean):
            while queue:
                i, j = queue.pop(0)
                if (i, j) in ocean:
                    continue
                ocean.add((i, j))
                for di, dj in directions:
                    ni, nj  = i+di, j+dj
                    if (0<=ni<m 
                    and 0<=nj<n 
                    and heights[ni][nj]>=heights[i][j]):
                        queue.append((ni, nj))

        bfs(pacific_start, pacific)
        bfs(atlantic_start, atlantic)
        out = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    out.append([i, j])
        return out