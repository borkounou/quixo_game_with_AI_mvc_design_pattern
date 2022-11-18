from .players import IPlayer
import random

class RandomPlayer(IPlayer):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.movable = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 4), (2, 0), (2, 4), (3, 0), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

    def __rnd(self, list_to_select):
        idx = random.randrange(0, len(list_to_select))
        return list_to_select[idx]

    def __chooser(self):
        pos1 = self.__rnd(self.movable)
        x = pos1[0]
        y = pos1[1]
        return x,y

    
    def playing(self,board,move,game_board,winner,player_turn):
        super().playing(board,move,game_board,winner,player_turn)
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
                board[x][y] = -1
                destination = game_board.get_possibles_destinations((x,y))
                secondeDestination = self.__rnd(destination)
                playerClick.append(secondeDestination)
              
                
                print(f"Destination to put the tile: {playerClick[1]}")
                move.move_tiles(board,playerClick[0],playerClick[1],-1)
                if winner.check_winner(board,-1)!=0:
                            print(winner.check_winner(board,-1))
                            print(f"player: {-1} wins!")
                playerClick=[]
                player_turn =True
                random =False
            
            return player_turn


    