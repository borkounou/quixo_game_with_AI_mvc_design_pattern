from .players import IPlayer

class SingleHumanPlayer(IPlayer):
    def __init__(self, name,game_board):
      
        self.name = name
        self.game_board = game_board

    def playing(self,x,y):
        if self.game_board.isGameEnd():
            self.game_board.reset_game()
            self.game_board.isGameEnd() is not self.game_board.isGameEnd()
            print("The game is over: There is no winner")
        if self.game_board.move.is_movable_piece(x,y):

            self.game_board.sq_selected = (y,x)
            self.game_board.player_click.append(self.game_board.sq_selected)
            destination = self.game_board.get_possibles_destinations(self.game_board.player_click[0])
            print(f"The possible destinations of the move {self.game_board.player_click[0]} are: {destination}")
            if len(self.game_board.player_click) == 1 and self.game_board.move.is_movable_piece(x,y):
                if self.game_board.board[y][x]!=0:
                    self.game_board.player_click.pop()
                    print("You can't put the same tile and same place")
                    pass 
                else:
                    self.game_board.board[y][x] = self.game_board.turn
                    
            if len(self.game_board.player_click) ==2:

                if self.game_board.player_click[1] in destination:
                    self.game_board.move.move_tiles(self.game_board.board,self.game_board.player_click[0],self.game_board.player_click[1],self.game_board.turn)
                    self.game_board.final_state(self.game_board.board, self.game_board.turn)

                    print(f"the len the playerclick is: {len(self.game_board.player_click)}")
                   
                    self.game_board.player_turn = not  self.game_board.player_turn
                    self.game_board.changeTurn()
                    self.game_board.player_click=[]
                  

                else:
                    print(f"{self.game_board.player_click[1]} is not a place to put a tile")
                    self.game_board.player_turn =  self.game_board.player_turn
                    self.game_board.player_click.pop()
                    pass

       
        # time.sleep(0.5)
        # return self.player_turn, self.board



    