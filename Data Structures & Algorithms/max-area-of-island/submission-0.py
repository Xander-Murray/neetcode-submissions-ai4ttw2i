class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        cnt = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def search(r,c):
            
            if r < 0 or c < 0 or r >= R or c >= C:
                return 0 
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                area += search(nr,nc)
            return area
            
            
                

            


        for r in range(R):
            for c in range(C):
                # we found start of island recusrsivly search
                if grid[r][c] == 1:
                    cnt = max(search(r,c), cnt)
                    
        return cnt
    