# Import the DIMENSION constant from the constants module
from constants import DIMENSION

class Move:
    
    def is_movable_piece(self,x,y):
        # Return True if the piece is located at the edge of the board (x or y equals 0 or 4)
        return x==0 or y==0 or x==4 or y ==4

    def get_movables_tiles(self,board,player_value=0):
        # Create an empty list to store the movable tiles
        movable = []
        # Iterate over the rows and columns of the board
        for x in range(DIMENSION):
            for y in range(DIMENSION):
                # Get the value at the current position
                value = board[x][y]
                # If the current position is a movable piece and the value is 0 or equal to the player value, add the position to the list of movable tiles
                if self.is_movable_piece(x,y) and (value ==0 or value ==player_value):
                    movable.append((x,y))
        # Return the list of movable tiles
        return movable
    
    def move_row(self, board,row,col_start,col_end,value):
        # Determine the step size for the loop based on whether col_end is greater or less than col_start
        step = -1 if col_end>col_start else 1
        # Determine the starting index for the loop based on the step size
        index_start = col_start-1 if col_end>col_start else col_start + 1
        # Iterate over the columns in the row
        for col in range(col_end, index_start,step):
            # Save the value at the current position
            prev_val = board[row][col]
            # Set the value at the current position to the given value
            board[row][col] = value
            # Update the value to the previous value
            value = prev_val

    def move_col(self,board,line,row_start,row_end,value):
        # Determine the step size for the loop based on whether row_end is greater or less than row_start
        step = -1 if row_end>row_start else 1
        # Determine the starting index for the loop based on the step size
        index_start = row_start - 1 if row_end > row_start else row_start + 1
        # Iterate over the rows in the column
        for x in range(row_end, index_start, step):
            # Save the value at the current position
            prev_val = board[x][line]
            # Set the value at the current position to the given value
            board[x][line] = value
            # Update the value to the previous value
            value = prev_val

    def move_tiles(self, board, pos_start,pos_end,value):
        # Unpack the start and end positions into row and column variables
        (row_start, col_start) = pos_start
        (row_end, col_end) = pos_end
        # If the start position is not a movable piece

        if not self.is_movable_piece(row_start,col_start):
            # Print an error message and exit the function
            print(f"This {(row_start, col_start)} is not a movable tile!")
            return
        
        # If the value at the start position is not 0 and is not equal to the given value
        if board[row_start][col_start] != 0 and board[row_start][col_start] != value:
            # Print an error message and exit the function
            print(f"Can't change the value of tile {row_start} - {col_start}")
            return

        # If the start and end rows are the same (i.e. the move is horizontal)
        if row_start == row_end:
            # Call the move_row function to move the tiles in the row
            self.move_row(board,row_start, col_start,col_end,value)
        
        # If the start and end columns are the same (i.e. the move is vertical)
        elif col_start == col_end:
            # Call the move_col function to move the tiles in the column
            self.move_col(board,col_start,row_start,row_end,value)
            
        # If the start and end positions are not in the same row or column
        else:
            # Print an error message
            print("Cannot move this tile to this position")

       