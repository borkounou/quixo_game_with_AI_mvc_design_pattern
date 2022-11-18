

class Move:
    def __init__(self):
        pass 

    
    def is_movable_piece(self, x,y):
        """
        Args: 
           -x: row position (from 0 to 4)
           -y: col position (from 0 to 4)
        return:
           - x:(0,0), (0,1), (0,2), (0,3), (0, 4)
              - (4,0), (4,1), (4,2), (4,3), (4,4)
           - y:

        """
        return x==0 or y==0 or x==4 or y==4

    def get_movables_tiles(self,board, player_value=0):
 
        movable = []
        for x in range(len(board)):
            for y in range(len(board[x])):
                value = board[x][y]
                if self.is_movable_piece(x, y) and (value == 0 or value == player_value):
                    movable.append((x, y))

        return movable

    

    def move_row(self, board, row,col_start, col_end,value):
        """
        @Params:
           - board: a list of lists
           - row : int (the specific movable row)
           - col_start: int (starting column)
           - col_end: int
           - value: int (1 for player 1 and 0 for player 2)
        
        @Return
           - board: a list of lists

        """

        step = -1 if col_end>col_start else 1
        index_start = col_start-1 if col_end>col_start else col_start+1
        for col in range(col_end, index_start, step):
           
            prev_val=board[row][col]
            board[row][col] = value
            value = prev_val
        # return board

    def move_col(self, board, line, row_start,row_end, value):
        """
        @Params:
           - board: a list of lists
           - row : int (the specific movable row)
           - col_start: int (starting column)
           - col_end: int
           - value: int (1 for player 1 and 0 for player 2)
        
        @Return
           - board: a list of lists

        """

        step = -1 if row_end > row_start else 1
        index_start = row_start - 1 if row_end > row_start else row_start + 1
        for x in range(row_end, index_start, step):
            prev_val = board[x][line]
            board[x][line] = value
            value = prev_val

        # return board

    

    def move_tiles(self,board,pos_start, pos_end, value):
        """
        It allows to move the tiles:
        
        @Params:
           - board: a list of list 
           - pos_start (starting position): tuple
           - pos_end (ending position): tuple
           - value: 1 for player 1 or -1 for player 2

        @Return 

           - board: a list of lists
        """

        (row_start, col_start) = pos_start
        (row_end, col_end) = pos_end
        if not self.is_movable_piece(row_start,col_start):
            print(f"This {(row_start, col_start)} is not a movable tile!")
            pass 
        else:
            if board[row_start][col_start] != 0 and board[row_start][col_start] != value:
                print(f"Can't change the value of tile {row_start} - {col_start}")
                pass 
            

            if row_start == row_end:
                self.move_row(board,row_start, col_start,col_end,value)
            
            elif col_start == col_end:
                self.move_col(board,col_start,row_start,row_end,value)
                
            else:
                print("Cannot move this tile to this position")

        
        
    