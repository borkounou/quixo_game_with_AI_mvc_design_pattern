
from .players import IPlayer
class PVPPlayer(IPlayer):
    def __init__(self, name):
        super().__init__(name)


    
    def playing(self, x, y):
        super().playing(x, y)
        if self.__move.is_movable_piece(x,y):
            self.__sqSelected = (y,x)
            self.__playerClick.append(self.__sqSelected)
            destination = self.__game_board.get_possibles_destinations(self.__playerClick[0])
            #Here to check if a specific square is empty and is movable
            if len(self.__playerClick) == 1 and self.__move.is_movable_piece(x,y):
                if self.__board[y][x]!=0:
                    self.__playerClick.pop()
                    print("You can't put the same tile and same place")
                    pass 
                else:
                    # self.__board[y][x]=1 if self.__player_turn else -1
                    self.__board[y][x] = self.__game_board.next_turn(self.__player_turn)

            
            if len(self.__playerClick) ==2:
                if self.__playerClick[1] in destination:
                    self.__move.move_tiles(self.__board,self.__playerClick[0],self.__playerClick[1],self.__game_board.next_turn(self.__player_turn))
                    if self.__winner.check_winner(self.__board,self.__game_board.next_turn(self.__player_turn))!=0:
                        print(self.__winner.check_winner(self.__board,self.__game_board.next_turn(self.__player_turn)))
                        print(f"player: {self.__game_board.next_turn(self.__player_turn)} wins!")
                        self.__restart_game()
                    self.__player_turn = not self.__player_turn
                    self.__playerClick=[]

                else:
                    print(f"{self.__playerClick[1]} is not a place to put a tile")
                    self.__playerClick.pop()
                    pass
