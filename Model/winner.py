from constants import DIMENSION,INDEX_LAST_ROW


"""
The objectif of this class is to implements the winning logic
"""
class Winner:

    def __init__(self):
        pass 

    def __find_winner(self,total):
        requirement = DIMENSION
        if total ==requirement:
            return 1
        if -total ==requirement:
            return -1 
        return 0
    
    def __check_winner_diagonale(self,board,inverted=False):
        sum_diagonal = 0
        for i in range(DIMENSION):
            x =i 
            y=i if not inverted else INDEX_LAST_ROW-i
            sum_diagonal+= board[x][y]
            
        return self.__find_winner(sum_diagonal)
    

    def __check_winner_rows(self, board, player=0):
        winner = 0 
        for row in board:
            temporary_winner = self.__find_winner(sum(row))
            if temporary_winner!=0:
                winner = temporary_winner
            if(winner<0 and player==-1) or (winner>0 and player==1):
                return winner
        return winner


    def __check_winner_cols(self, board,player=0):
        # invert cols and rows
        inverted_board = list(map(list, zip(*board)))
        return self.__check_winner_rows(inverted_board, player)

    def check_winner(self, board, player=0):
        first_diagonale = self.__check_winner_diagonale(board)
        seconde_diagonale = self.__check_winner_diagonale(board, True)
        rows = self.__check_winner_rows(board, player)
        cols = self.__check_winner_cols(board, True)
        winner  = 0
        winner_result_list = [first_diagonale, seconde_diagonale, rows, cols]
        for result in winner_result_list:
            if result!=0:
                winner = result
            if winner==-1 and player==-1 or winner ==1 and player==1:
                return winner # 0, -1 or 1
        return winner # 0, -1 or 1

