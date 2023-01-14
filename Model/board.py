import numpy as np 
from constants import DIMENSION, SQ_SIZE,IMAGE_SIZE
from constants import INDEX_LAST_COL,INDEX_LAST_ROW
from .move import Move
from .winner import Winner

class GameState:
    X = 1 # Human Player
    O = -1 # AI player
    BLANK = 0 # Empty no player
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def __init__(self, board=None, turn=1):
        self.board = self.__create_board() if board is None else board.board
        self.turn = turn if board is not None else 1
        # move class
        self.move = Move()
        # Winner class 
        self.ai_move = None
        self.winner_state =None
        self.winner = Winner()
        self.player_turn = True
        self.sq_selected = ()
        self.player_click = []
        self.running = True
        self.start_game = False
        self.movable = self.move.get_movables_tiles(self.board)

    # Create the board using numpy of zeros
    def __create_board(self):

        return np.zeros((DIMENSION, DIMENSION), dtype=int)

    # Play the game
    def play(self,board,piece,move):
        board[piece] =self.turn
        self.move.move_tiles(board,piece,move,self.turn)
        self.changeTurn()

    def get_possible_moves(self):
        allMoves = []
        for piece in self.movable:
            moves = self.get_possibles_destinations(piece)
            for move in moves:
                allMoves.append((piece,move))
        np.random.shuffle(allMoves)
        return allMoves

    
    def gameOver(self):
        self.running = False

    def changeTurn(self):
        if(self.turn ==self.X):
            self.turn = self.O
        else:
            self.turn = self.X

    
    def isGameEnd(self):
        return all(self.board[index]!=0 for index in self.movable)

    
    def isGameEndFinal(self):

        """Determine if the game has ended in a win or a draw.

        Returns:
        int: The value of the winning player (either self.X, self.O, or self.BLANK) if the game has ended in a win or a draw, or 0 otherwise.
        """
        first_diagonal = np.diagonal(self.board)
        second_diagonal = np.diagonal(np.rot90(self.board))
        if np.all(first_diagonal == self.X) or np.all(first_diagonal == self.O):
            return self.board[0, 0]
        if np.all(second_diagonal == self.X) or np.all(second_diagonal == self.O):
            return self.board[0, INDEX_LAST_ROW]

        for i in range(0, INDEX_LAST_ROW + 1):
            row = self.board[i, :]
            col = self.board[:, i]
            if np.all(row == self.X) or np.all(row == self.O):
                return self.board[i, 0]
            if np.all(col == self.X) or np.all(col == self.O):
                return self.board[0, i]

        return 0
    
    def reset_game(self):
        self.__init__()
    
    def start_player(self, x,y):
        position = [(1,2),(3,2)]
        if (x,y) in position:
            if (x,y)==position[0]: self.turn=self.X
            if (x,y)==position[1]: self.turn = self.O
           

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
        """Return a list of possible destinations for a given position.

        Parameters:
        pos_end (tuple): The position for which to find possible destinations.

        Returns:
        list: A list of tuples representing the possible destinations.
        """
        destinations = []
        (x, y) = pos_end

        if x in (0, INDEX_LAST_ROW):
            if y != 0:
                destinations.append((x, 0))
            if y != INDEX_LAST_COL:
                destinations.append((x, INDEX_LAST_COL))
            opposite = 0 if x == INDEX_LAST_ROW else INDEX_LAST_ROW
            destinations.append((opposite, y))

        if (y in (0, INDEX_LAST_COL)) and (x not in (0, INDEX_LAST_ROW)):
            if x != 0:
                destinations.append((0, y))
            if x != INDEX_LAST_ROW:
                destinations.append((INDEX_LAST_COL, y))
            opposite = 0 if y == INDEX_LAST_COL else INDEX_LAST_COL
            destinations.append((x, opposite))

        return destinations


    
