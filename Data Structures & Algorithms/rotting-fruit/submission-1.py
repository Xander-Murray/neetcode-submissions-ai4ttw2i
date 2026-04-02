class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        q = deque()
        fresh = 0
        time = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    
                    # Bounds check and check if FRESH (1)
                    # Note: We don't need a 'visit' set. If it's 1, it's unvisited.
                    if (nr < 0 or nc < 0 or 
                        nr >= R or nc >= C or 
                        grid[nr][nc] != 1):
                        continue
                    
                    # Infect the neighbor
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
            
            # 3. Increment time only after processing the whole batch
            time += 1
        return time if fresh == 0 else -1


