class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        cells = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val.isdigit():
                    if val in rows[i]:
                        # print("Row", val, rows[i])
                        return False
                    if val in cols[j]:
                        # print("Col", val, cols[j])
                        return False
                    cell_row = i//3
                    cell_col = j//3
                    cell_id = cell_row*3+cell_col
                    if val in cells[cell_id]:
                        # print("Cell", val, cells[cell_id])
                        return False
                    rows[i].add(val)
                    cols[j].add(val)
                    cells[cell_id].add(val)
        return True