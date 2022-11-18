
from .single_human_player import SingleHumanPlayer
from .random_player import RandomPlayer 
from .aiplayer import Ai
class PlayersFactory:
    def __init__(self):
        pass
    @staticmethod
    def play(player_name):
        if player_name =="random":
            return RandomPlayer(player_name)
        
        if player_name=="human":
            return SingleHumanPlayer(player_name)

        if player_name=="ai":
            return Ai("ai")
        if player_name =="pvp":
            return 

        else:
            return None