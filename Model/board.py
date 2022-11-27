import numpy as np 
from constants import DIMENSION, SQ_SIZE,IMAGE_SIZE
from constants import INDEX_LAST_COL,INDEX_LAST_ROW
from .move import Move
from .winner import Winner
class Board:
    X = 1
    O = -1 
    BLANK = 0

    def __init__(self, board=None, turn=1):
        if (board ==None):
            self.board = self.__create_board()
            self.turn = turn 
        else:
            self.board = board.board
            self.turn = board.turn

        # move class
        self.move = Move()
        # Winner class 
        self.winner = Winner()

        self.player_turn = True
        self.sq_selected = ()
        self.player_click = []
        self.running = True
        self.start_game = False
        self.movable = self.move.get_movables_tiles(self.board)


    def __create_board(self):
        return np.zeros((DIMENSION, DIMENSION), dtype=int)

    
    def gameOver(self):
        self.running = False

    def changeTurn(self):
        if(self.turn ==self.X):
            self.turn = self.O
        else:
            self.turn = self.X

    
    def isGameEnd(self):
        return all(self.board[index]!=0 for index in self.movable)

    
    def reset_game(self):
        self.__init__()
    

    def start_player(self, x,y):
        position = [(1,2),(3,2)]
        if (x,y) in position:
            if (x,y)==position[0]: self.turn=self.X#self.player_turn = True 
            if (x,y)==position[1]: self.turn = self.O#self.player_turn = False
           
        # return self.player_turn

    def get_mouse_coordinate(self, pos):
        x = int((pos[0]-SQ_SIZE)/IMAGE_SIZE)
        y = int((pos[1]-SQ_SIZE)/IMAGE_SIZE)
        if x<0:x=0
        if x>4: x=4
        if y<0: y=0
        if y>4: y=4
        return x,y

    

    def final_state(self,board,turn):

        if self.winner.winner_check(board)==turn:
                    print(self.winner.winner_check(board))
                    print(f"player: {self.winner.winner_check(board)} wins!")
            
        else:
            if not self.isGameEnd():
                print("The game is running and the players are playing")
                print(f"It is player {self.turn} turn")

            else:
                self.end = True
                self.reset_game()


    def get_possibles_destinations(self, pos_end):
        destinations = []
        (x,y) = pos_end
        if x == 0 or x == INDEX_LAST_ROW:
            if y != 0:
                destinations.append((x, 0))
            if y != INDEX_LAST_COL:
                destinations.append((x, INDEX_LAST_COL))
            opposite = 0 if x == INDEX_LAST_ROW else INDEX_LAST_ROW
            destinations.append((opposite, y))

        if (y == 0 or y == INDEX_LAST_COL) and (x != 0 and x != INDEX_LAST_ROW):
            if x != 0:
                destinations.append((0, y))
            if x != INDEX_LAST_ROW:
                destinations.append((INDEX_LAST_COL, y))
            opposite = 0 if y == INDEX_LAST_COL else INDEX_LAST_COL
            destinations.append((x, opposite))

        return destinations
    
