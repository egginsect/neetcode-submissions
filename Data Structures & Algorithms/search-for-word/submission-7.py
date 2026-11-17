from functools import cache
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        m = len(board)
        n = len(board[0])

        def dfs(i, j, idx):
            if word[idx] != board[i][j]:
                return False
            if idx == len(word)-1:
                return True
            
            temp = board[i][j]
            board[i][j] = '#'
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<m and 0<=nj<n and idx+1<len(word):
                    if dfs(ni, nj, idx+1):
                        return True
            board[i][j] = temp
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False