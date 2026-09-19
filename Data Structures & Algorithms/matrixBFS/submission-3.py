class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        columns=len(grid[0])

        def bfs(row,column):
            directions=[(0,1),(1,0),(-1,0),(0,-1)]
            visited = {(row,column)}
            path_length=0
            #We need to build a Queue
            queue=[(row,column,0)]

            #distance from start to current node
            while len(queue)>0:
                current_node= queue.pop(0)
                distance=current_node[2]
                if current_node[0] == len(grid)-1 and current_node[1] == len(grid[0])-1:
                    return distance
                for r,c in directions:  
                    new_row=current_node[0]+r
                    new_column=current_node[1]+c
                    
                    if (
                        0 <= new_row < len(grid)
                        and 0 <= new_column < len(grid[0])
                        and grid[new_row][new_column] == 0
                        and (new_row, new_column) not in visited
                    ):  

                        visited.add((new_row,new_column))
                        queue.append((new_row,new_column,distance+1))
        
    

            
            return -1
            #check if the last node is the final node 
        

        if(grid[0][0]==0):
            length=bfs(0,0)
            return length
        else:
            return -1
    
        
        