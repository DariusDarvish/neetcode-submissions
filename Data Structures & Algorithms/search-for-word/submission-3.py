class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        visited_cells=set()
        rows=len(board)
        columns=len(board[0])

        #dfs
        def dfs(r,c,word):
            if len(word)==0:
                return True
            visited_cells.add((r,c))

            for row,column in directions:
                new_row=r+row
                new_column=c+column
                if(new_row in range(rows) and new_column in range(columns) and
                (new_row,new_column) not in visited_cells and board[new_row][new_column]==word[0]
                ):
                    if(dfs(new_row,new_column,word[1::])):
                        return True
            visited_cells.remove((r,c))
            return False


        for row in range(rows):
            for column in range(columns):
                if board[row][column]==word[0] and (row,column) not in visited_cells:
                    val=dfs(row,column,word[1::])
                    if(val==True):
                            return True
        return False
        