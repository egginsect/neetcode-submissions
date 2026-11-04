from collections import defaultdict
class TicTacToe:

    def __init__(self, n: int):
        self.p1 = defaultdict(int)
        self.p2 = defaultdict(int)
        self.end = False
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        current = self.p1 if player == 1 else self.p2
        if row == col:
            current["diag"] += 1
        if row+col == self.n-1:
            current["antidiag"] += 1
        current[f"({row},)"] += 1
        current[f"(,{col})"] += 1
        for val in current.values():
            if val == self.n:
                self.end = True
                return player
        return 0

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
