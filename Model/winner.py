from constants import DIMENSION,INDEX_LAST_ROW
from constants import SQ_SIZE, IMAGE_SIZE,WIDTH,HEIGHT
import pygame


"""
The objectif of this class is to implements the winning logic
"""
class Winner:
    
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
            print(row)
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

    def winner_check(self,board,show=False):
            '''
            @return 0 if there is  no win yet
            @return 1 if player 1 wins
            @return 2 if player 2 wins
            '''
            #Vertical wins
            for col in range(DIMENSION):
                if board[0][col] == board[1][col] == board[2][col]== board[3][col]==board[4][col]:
                    # SQ_SIZE + 1*IMAGE_SIZE,SQ_SIZE + 2*IMAGE_SIZE
                    # iPos = (col * IMAGE_SIZE+SQ_SIZE + SQ_SIZE//2, 20)
                    # fPos = (col * IMAGE_SIZE+SQ_SIZE + SQ_SIZE//2, HEIGHT-20)
                    # print(iPos, fPos)
                    # pygame.draw.line(screen, "black", iPos, fPos, 20)


            
                    if board[0][col] == -1:
                        return - 1
                    if board[0][col] ==1:
                        return 1
                        
            #Horizontal wins
            for row in range(DIMENSION):
                if board[row][0] == board[row][1] == board[row][2]== board[row][3]==board[row][4]!=0:

                    if board[row][0] ==-1:
                        return -1
                    if board[row][0] ==1:
                        return 1
            
            # Desc diagonal 
            if board[0][0] == board[1][1] == board[2][2]==board[3][3] ==board[4][4] !=0:
                  if board[2][2] == -1:
                    return -1
                  if board[2][2] ==1:
                    return 1
                
            # Asc diagonal 

            if board[4][0] == board[3][1] == board[2][2]==board[1][3] ==board[0][4] !=0:

                if board[2][2] ==-1:
                    return -1
                if board[2][2] ==1:
                    return 1
            
            # no win yet
            else:
                return 0



