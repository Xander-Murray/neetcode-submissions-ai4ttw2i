class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        cnt = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def search(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return
            if grid[r][c] == '0':
                return
            grid[r][c] = '0'
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                search(nr,nc)
            
                

            

        # nested for loop until you find a 1
        # once you find a one check adjacent directions
        # if 0 return
        # if 1 keep searching as soon as all return count += 1 also when you get to a one change it to a 0

        for r in range(R):
            for c in range(C):
                # we found start of island recusrsivly search
                if grid[r][c] == '1':
                    cnt += 1
                    search(r,c)
        return cnt
    

        