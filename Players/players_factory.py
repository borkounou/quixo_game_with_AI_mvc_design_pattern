
from .single_human import SingleHumanPlayer
from .random_player import RandomPlayer 
from .ai_player import AIPlayer
# from ai_player import Ai
class PlayersFactory:
    def __init__(self,game_board):
        self.game_board = game_board

    def play(self,player_name):
        if player_name =="random":
            return RandomPlayer(player_name,self.game_board)
        
        if player_name=="human":
            return SingleHumanPlayer(player_name,self.game_board)

        
        if player_name=="ai":
            return AIPlayer(player_name,self.game_board)

        else:
            return None