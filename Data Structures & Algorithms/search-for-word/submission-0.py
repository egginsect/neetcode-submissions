class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        path = set()
        def dfs(i, j, length=0):
            if length == len(word):
                return True
            if i==m or j==n or min(i, j)<0 or board[i][j] != word[length] or (i,j) in path:
                return False
            path.add((i, j))
            if any([dfs(i-1, j, length+1), 
            dfs(i+1, j, length+1), 
            dfs(i, j-1, length+1), 
            dfs(i, j+1, length+1)]):
                return True
            path.remove((i, j))
            return False
        for i in range(m):
            for j in range(n):
                if dfs(i, j):
                    return True
        return False
            
        