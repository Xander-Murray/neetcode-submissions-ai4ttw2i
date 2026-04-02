class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        R, C = len(heights), len(heights[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(r, c, visit, prevHeight):
            if ((r,c) in visit or r < 0 or 
            c < 0 or r== R or c== C or heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr, nc, visit, heights[r][c])

        # every column in first row
        for c in range(C):
            dfs(0, c, pac, heights[0][c])
            dfs(R - 1, c, atl, heights[R - 1][c])

        for r in range(R):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, C - 1, atl, heights[r][C - 1])

        return list(pac & atl)
