
import pygame

class Controller:

    def __init__(self, Game_board, Move, Winner,View,players):
        pygame.init()
        self.__game_board = Game_board
        self.__move = Move
        self.__winner = Winner
        self.__view = View
        self.__screen = self.__view.screen
        self.__board = self.__game_board.board
        self.__player_turn = self.__game_board.cross_turn
        self.__sqSelected = self.__game_board.sq_selected
        self.__playerClick = self.__game_board.player_click
        self.__running = self.__game_board.running
        self.__starting_game =  self.__game_board.start_game
        self.players = players
        

    def __restart_game(self):
        self.__game_board.reset_game()
        self.__init__(self.__game_board, self.__move, self.__winner,self.__view,self.random_player)

    
    def __play(self, x,y):
       
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

    def __playing(self, x,y):
        if self.__move.is_movable_piece(x,y):
            self.__sqSelected = (y,x)
            self.__playerClick.append(self.__sqSelected)
            destination = self.__game_board.get_possibles_destinations(self.__playerClick[0])
            if len(self.__playerClick) == 1 and self.__move.is_movable_piece(x,y):
                if self.__board[y][x]!=0:
                    self.__playerClick.pop()
                    print("You can't put the same tile and same place")
                    pass 
                else:
                    self.__board[y][x] = 1
            
            

            if len(self.__playerClick) ==2:

                if self.__playerClick[1] in destination:
                    self.__move.move_tiles(self.__board,self.__playerClick[0],self.__playerClick[1],1)
                    if self.__winner.check_winner(self.__board,1)!=0:
                        print(self.__winner.check_winner(self.__board,1))
                        print(f"player: {1} wins!")
                    self.__player_turn = not self.__player_turn
                    self.__playerClick=[]

                else:
                    print(f"{self.__playerClick[1]} is not a place to put a tile")
                    self.__player_turn = self.__player_turn
                    self.__playerClick.pop()
                    pass
       

        return self.__player_turn 



    def main_loop(self):
        while self.__running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running =False

                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.__restart_game()

                if event.type == pygame.MOUSEBUTTONDOWN and self.__starting_game ==False:
                    pos = pygame.mouse.get_pos()
                    x,y = self.__game_board.get_mouse_coordinate(pos)
                    self.__starting_game = True
                    self.__player_turn = self.__game_board.start_player(x,y)

                if event.type == pygame.MOUSEBUTTONDOWN and self.__starting_game:
                    pos = pygame.mouse.get_pos()
                    x,y = self.__game_board.get_mouse_coordinate(pos)
                    self.__play(x,y)
    
            
            if not self.__starting_game:
                # Welcome screen 
                screen = self.__view.build_screen("welcome_screen")
                screen.draw_screen(self.__screen)
            else:
                # Main screen 
                screen = self.__view.build_screen("main_screen")
                screen.draw_screen(self.__screen, self.__board)

            pygame.display.update()
            self.__view.clock.tick(50)



    def main_loop_test(self):
        while self.__running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running =False

                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.__restart_game()

                if event.type == pygame.MOUSEBUTTONDOWN and self.__starting_game ==False:
                    pos = pygame.mouse.get_pos()
                    x,y = self.__game_board.get_mouse_coordinate(pos)
                    self.__starting_game = True
                    self.__player_turn = self.__game_board.start_player(x,y)

                if event.type == pygame.MOUSEBUTTONDOWN and self.__starting_game==True:
                    pos = pygame.mouse.get_pos()
                    x,y = self.__game_board.get_mouse_coordinate(pos)
                    self.__player_turn=self.__playing(x,y)
                    # player3 = self.players.play('human')
                    # self.__player_turn= player3.playing(self.__board, pos, self.__move, self.__game_board, self.__winner, self.__player_turn)
                    print(self.__player_turn)
                   
                    
                
                if self.__player_turn ==False:
                    player2 = self.players.play("random")
                    self.__player_turn = player2.playing(self.__board,pos,self.__move, self.__game_board, self.__winner,self.__player_turn)
                  
                    # self.__player_turn = self.players.playing(self.__board,self.__move, self.__game_board, self.__winner,self.__player_turn)
                    
                    
    
                
            
            
            if not self.__starting_game:
                # Welcome screen 
                screen = self.__view.build_screen("welcome_screen")
                screen.draw_screen(self.__screen)
            else:
                # Main screen 
                screen = self.__view.build_screen("main_screen")
                screen.draw_screen(self.__screen, self.__board)

            pygame.display.update()
            self.__view.clock.tick(50)
            
            
                       
                    

















