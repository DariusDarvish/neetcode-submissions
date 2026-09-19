class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited_cells=set()
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        rows=len(board)
        columns=len(board[0])

        #def DFS
        def dfs(r,c,word):
           #base case
            if len(word)==0:
                return True
            #Search the nodes in every direction
            visited_cells.add((r,c))
            for row,col in directions:
                new_row=r+row
                new_col=c+col
                if(new_row in range(rows) and new_col in range(columns)
                and (new_row,new_col) not in visited_cells
                and board[new_row][new_col]==word[0]
                ):
                    if dfs(new_row,new_col,word[1::]):
                        return True
            visited_cells.remove((r,c))
            return False




        for row in range(rows):
            for col in range(columns):
                if board[row][col] == word[0]:
                    #dfs search
                    if(len(word)==1):
                        return True
                    result=dfs(row,col,word[1::])
                    if result==True:
                        return True
                  
        return False
        