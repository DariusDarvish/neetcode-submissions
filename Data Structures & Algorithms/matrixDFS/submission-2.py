class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        columns=len(grid[0])
        count=0
        visisted=set()

        def dfs(row,column):
            nonlocal count
            nonlocal grid
            nonlocal visisted
            nonlocal rows
            nonlocal columns
            moves=[(0,1),(1,0),(0,-1),(-1,0)]
            if row == rows - 1 and column == columns - 1 and grid[row][column]==0:
                count+=1
                return count
            visisted.add((row,column))
            for r,c in moves:
                new_row=row+r
                new_column=column+c
                if(0 <= new_row < len(grid) and 0 <= new_column < len(grid[0])
                and grid[new_row][new_column]==0 and (new_row,new_column) not in visisted):
                    dfs(new_row,new_column)
            visisted.remove((row,column))
            return count
        if (grid[0][0]==0):
            dfs(0,0)
        else:
            return 0
        return count

        