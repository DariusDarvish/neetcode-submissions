class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
         we want to use BFS to check all the cells with in one place
         of the current cell we are looking at
         if the cell is not visisted we add the cell to the queue and check
         the rest
        '''
        visited=set()
        total_island_count=0
        rows=len(grid)
        cols=len(grid[0])
        direction=[[1,0],[0,1],[-1,0],[0,-1]]
       
        #BFS search
        def bfs(r,c):
            queue=[]
            visited.add((r,c))
            queue.append((r,c))
            while(queue):
                r,c=queue.pop()
                for row,col in direction:
                    row_cord=r+row
                    col_cord=c+col
                    '''
                    If graph[row_cord][col_cord] are in grid 
                    and graph[row_cord][col_cord] are not in visited
                    and graph[row_cord][col_cord] =="1"
                    '''
                    if(row_cord in range(rows) and
                    col_cord in range(cols) and
                    (row_cord,col_cord)not in visited
                    and grid[row_cord][col_cord]=="1"):
                        visited.add((row_cord,col_cord))
                        queue.append((row_cord,col_cord))

        #Getting first "1"
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1" and (row,col) not in visited:
                    bfs(row,col)
                    total_island_count+=1
        
        return total_island_count

