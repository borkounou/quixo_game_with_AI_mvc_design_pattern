from .players import IPlayer

class SingleHumanPlayer(IPlayer):
    def __init__(self, name, game_board):
        self.name = name
        self.__game_board = game_board

    def playing(self, x, y):
        # Check if game is over and reset if necessary
        if self.__game_board.isGameEnd():
            self.__game_board.reset_game()
            # Double check that game is not over after reset
            if self.__game_board.isGameEnd():
                self.__game_board.winner_state = "Draw:no winner"

        # Check if square is a movable piece
        if self.__game_board.move.is_movable_piece(x, y):
            self.__game_board.sq_selected = (y, x)
            self.__game_board.player_click.append(self.__game_board.sq_selected)

            # Get possible destinations for piece
            destinations = self.__game_board.get_possibles_destinations(self.__game_board.player_click[0])
            print(f"The possible destinations of the move {self.__game_board.player_click[0]} are: {destinations}")

            # If this is the first player click, place a tile on the square if it is not already occupied
            if len(self.__game_board.player_click) == 1:
                if self.__game_board.board[y][x] != 0:
                    self.__game_board.player_click.pop()
                    print("You can't put a tile in the same place")
                else:
                    self.__game_board.board[y][x] = self.__game_board.turn

            # If this is the second player click, check if selected square is a valid destination
            if len(self.__game_board.player_click) == 2:
                if self.__game_board.player_click[1] in destinations:
                    # Move piece to destination
                    self.__game_board.move.move_tiles(self.__game_board.board, self.__game_board.player_click[0],
                                                    self.__game_board.player_click[1], self.__game_board.turn)
                    # Check if game is over and update winner state
                    state = self.__game_board.isGameEndFinal()
                    if state == self.__game_board.turn:
                        self.__game_board.winner_state = "Human wins"
                    elif state != self.__game_board.turn and state != 0:
                        self.__game_board.winner_state = "AI wins"
                    elif self.__game_board.isGameEnd():
                        self.__game_board.winner_state = "Draw:no winner"
                        print(self.__game_board.winner_state)
                    else:
                        print(self.__game_board.winner_state)

                    # Switch turns and reset player clicks
                    self.__game_board.player_turn = not self.__game_board.player_turn
                    self.__game_board.changeTurn()
                    self.__game_board.player_click = []
                else:
                    # If selected square is not a valid destination, remove it from player clicks and stay on same turn
                    print(f"{self.__game_board.player_click[1]} is not a valid destination")
                    self.__game_board.player_turn = self.__game_board.player_turn
                    self.__game_board.player_click.pop()


