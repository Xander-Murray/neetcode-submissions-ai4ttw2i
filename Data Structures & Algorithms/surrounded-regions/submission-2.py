class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]



        def dfs(r, c):
            if (r < 0 or c < 0 or r >= R or c >= C or board[r][c] != "O"):
                return
            if board[r][c] == "O":
                board[r][c] = "#"
            
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)

        for c in range(C):
            if board[0][c] == "O":
                dfs(0, c)
            if board[R-1][c] == "O":
                dfs(R-1, c)

        for r in range(R):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][C - 1] == "O":
                dfs(r, C - 1)

        for r in range(R):
            for c in range(C):
                if board[r][c] == "#":
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        