class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        
        islands = 0
        visit = set() # tuple of row,col
        
        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            
            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                
                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    
                    if new_row < ROWS and new_row >= 0 and new_col >= 0 and new_col < COLS and                     (new_row,new_col) not in visit and grid[row][col] == "1":
                            # print(f"visit: {visit}")
                            # print(f"islands: {islands}")
                            visit.add((new_row,new_col))
                            q.append((new_row,new_col))
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    # print(f"r: {r} c: {c} ")
                    islands += 1
                    bfs(r,c)
                    
        for r in range(ROWS):
            for c in range(COLS):
                print(grid[r][c], end= ' ')
            print()
        
        return islands
                