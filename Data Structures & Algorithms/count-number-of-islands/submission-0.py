class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows,cols=len(grid),len(grid[0])
        visited=set()
        islands=0

        #searchs for all the 1 connected orignal 1
        def bfs(row,col):
            directions=[[1,0],[0,1],[-1,0],[0,-1]]
            visited.add((row,col))
            queue=[]
            queue.append((row,col))
            while(queue):
                row,col=queue.pop()
                for dr , dc in directions:
                    if ((row+dr) in range(rows) and 
                        (col+dc) in range(cols) and grid[row+dr][col+dc]=="1"
                        and(row+dr,col+dc) not in visited):
                        queue.append((row+dr,col+dc))
                        visited.add((row+dr,col+dc))

        #Finds the first 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    #BFS
                    bfs(r,c)
                    islands+=1
                
        return islands

        