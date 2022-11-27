from .players import IPlayer
import random
import time


class RandomPlayer(IPlayer):
    def __init__(self, name,game_board):
        # super().__init__(name,game_board)
        self.name = name
        self.game_board=game_board
        self.end = False

    def __rnd(self, list_to_select):
        idx = random.randrange(0, len(list_to_select))
        return list_to_select[idx]


    def __chooser(self):
        pos1 = self.__rnd(self.game_board.movable)
        x = pos1[0]
        y = pos1[1]
        return x,y
    
    def playing(self,board):
        super().playing(board)
        playerClick = []
        random = True
        while random:
            x,y = self.__chooser()
            playerClick.append((x,y))
            if board[x][y]!=0:
                playerClick.pop()
                continue     
            if board[x][y]==0:
                print(f"Choosen first option: {playerClick[0]}")
                board[x][y] = self.game_board.turn
                # time.sleep(0.5)
                destination = self.game_board.get_possibles_destinations((x,y))
                secondeDestination = self.__rnd(destination)
                # time.sleep(wait)
                playerClick.append(secondeDestination)
                print(f"Destination to put the tile: {playerClick[1]}")
                self.game_board.move.move_tiles(board,playerClick[0],playerClick[1],self.game_board.turn)
                self.game_board.final_state(self.game_board.board, self.game_board.turn)

                playerClick=[]
                self.game_board.player_turn = not self.game_board.player_turn
                self.game_board.changeTurn()
                random =False
           


    