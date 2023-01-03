# Import the DIMENSION constant from the constants module
from constants import DIMENSION

"""
The objectif of this class is to implements the winning logic
"""
class Winner:
    def winner_check(self,board):

        '''
        @return 0 if there is  no win yet
        @return 1 if player 1 wins
        @return -1 if player 2 wins
        '''
        # Check for vertical wins
        for col in range(DIMENSION):
            # If all the values in the column are the same and not 0, return the value (1 or -1)
            if board[0][col] == board[1][col] == board[2][col]== board[3][col]==board[4][col] != 0:
                return board[0][col]
        
        # Check for horizontal wins
        for row in range(DIMENSION):
            # If all the values in the row are the same and not 0, return the value (1 or -1)
            if board[row][0] == board[row][1] == board[row][2]== board[row][3]==board[row][4] != 0:
                return board[row][0]
        
        # Check for descending diagonal wins
        if board[0][0] == board[1][1] == board[2][2]==board[3][3] ==board[4][4] != 0:
            # Return the value at the center of the diagonal (1 or -1)
            return board[2][2]

        # Check for ascending diagonal wins
        if board[4][0] == board[3][1] == board[2][2]==board[1][3] ==board[0][4] != 0:
            # Return the value at the center of the diagonal (1 or -1)
            return board[2][2]

        # If no win has been detected, return 0
        return 0

