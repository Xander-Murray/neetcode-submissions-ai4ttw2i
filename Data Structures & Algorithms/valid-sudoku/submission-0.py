class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        grids = defaultdict(set) # key = (r / 3, c / 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in grids[r //3, c// 3]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grids[r // 3, c // 3].add(board[r][c])
        return True
        