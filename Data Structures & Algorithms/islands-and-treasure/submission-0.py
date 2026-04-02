class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R = len(grid)
        C = len(grid[0])
        q = deque()
        visit = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        

        for r in range(R):
            for c in range(C):
                # we found start of island recusrsivly search
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
            
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (nr < 0 or nc < 0 or nr >= R
                 or nc >= C or (nr, nc) in 
                 visit or grid[nr][nc] == -1):
                    continue
                

                visit.add((nr,nc))
                q.append((nr,nc))
                grid[nr][nc] = grid[r][c] + 1
        