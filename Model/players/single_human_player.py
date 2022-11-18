from .players import IPlayer
from Model.board import Board

class SingleHumanPlayer(IPlayer):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def playing(self,board,pos, move, game_board, winner, player_turn):
        super().playing(board, pos, move, game_board, winner, player_turn)
        sqSelected =()
        playerClick = []
        x,y = game_board.get_mouse_coordinate(pos)
        if move.is_movable_piece(x,y):
            sqSelected = (y,x)
            playerClick.append(sqSelected)
            destination = game_board.get_possibles_destinations(playerClick[0])
            if len(playerClick) == 1 and move.is_movable_piece(x,y):
                if board[y][x]!=0:
                    playerClick.pop()
                    print("You can't put the same tile and same place")
                    pass 
                else:
                    board[y][x] = 1
            
            if len(playerClick) ==2:

                if playerClick[1] in destination:
                    move.move_tiles(board,playerClick[0],playerClick[1],1)
                    if winner.check_winner(board,1)!=0:
                        print(winner.check_winner(board,1))
                        print(f"player: {1} wins!")
                    player_turn = False
                    playerClick=[]

                else:
                    print(f"{playerClick[1]} is not a place to put a tile")
                    player_turn = player_turn
                    playerClick.pop()
                    pass
       

        return player_turn 



    