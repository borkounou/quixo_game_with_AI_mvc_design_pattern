import pygame
from constants import IMAGE_SIZE, SQ_SIZE

class QuixoController:
    def __init__(self, Game_board, Move, Winner,QuixoView):
        pygame.init()
        self.game_board = Game_board
        self.move = Move
        self.winner = Winner
        self.view = QuixoView
        self.__screen = self.view.screen
        self.__board = self.game_board.board
        self.__player_turn = self.game_board.player_id
        self.__sqSelected = self.game_board.sq_selected
        self.__playerClick = self.game_board.player_click
        self.__running = self.game_board.running
        

        
    def __get_mouse_coordinate(self, pos):
        x = int((pos[0]-SQ_SIZE)/IMAGE_SIZE)
        y = int((pos[1]-SQ_SIZE)/IMAGE_SIZE)
        if x<0:x=0
        if x>4: x=4
        if y<0: y=0
        if y>4: y=4
        return x,y



    def __play2(self, x,y):
       
        if self.move.is_movable_piece(x,y):
            self.__sqSelected = (y,x)
            self.__playerClick.append(self.__sqSelected)
            destination = self.game_board.get_possibles_destinations(self.__playerClick[0])
            #Here to check if a specific square is empty and is movable
            if len(self.__playerClick) == 1 and self.move.is_movable_piece(x,y):
                if self.__board[y][x]!=0:
                    self.__playerClick.pop()
                    print("You can't put the same tile and same place")
                    pass 
                else:
                    # self.__board[y][x]=1 if self.__player_turn else -1
                    self.__board[y][x] = self.game_board.next_turn(self.__player_turn)

            
            if len(self.__playerClick) ==2:

                if self.__playerClick[1] in destination:
                    self.move.move_tiles(self.__board,self.__playerClick[0],self.__playerClick[1],self.game_board.next_turn(self.__player_turn))
                    if self.winner.check_winner(self.__board,self.game_board.next_turn(self.__player_turn))!=0:
                        print(self.winner.check_winner(self.__board,self.game_board.next_turn(self.__player_turn)))
                        print(f"player: {self.game_board.next_turn(self.__player_turn)} wins!")
                        self.game_board.reset_game()
                        self.__init__(self.game_board, self.move, self.winner,self.view)
                    self.__player_turn = not self.__player_turn
                    self.__playerClick=[]

                else:
                    print(f"{self.__playerClick[1]} is not a place to put a tile")
                    self.__playerClick.pop()
                    pass

    
    def __play(self, x,y):
       
        if self.move.is_movable_piece(x,y):
            self.__sqSelected = (y,x)
            self.__playerClick.append(self.__sqSelected)
            destination = self.game_board.get_possibles_destinations(self.__playerClick[0])
            #Here to check if a specific square is empty and is movable
            if len(self.__playerClick) == 1 and self.move.is_movable_piece(x,y):
                if self.__board[y][x]!=0:
                    self.__playerClick.pop()
                    print("You can't put the same tile and same place")
                    pass 
                else:
                    self.__board[y][x]=1 if self.__player_turn else -1

            
            if len(self.__playerClick) ==2 and self.__player_turn:

                if self.__playerClick[1] in destination:

                    self.move.move_tiles(self.__board,self.__playerClick[0],self.__playerClick[1],1)
                    if self.winner.check_winner(self.__board,1)!=0:
                        print("Player 1 wins:")
                    self.__player_turn = not self.__player_turn
                    self.__playerClick=[]
                else:
                    print(f"{self.__playerClick[1]} is not a place to put a tile")
                    self.__playerClick.pop()
                    pass

            elif len(self.__playerClick) ==2 and  self.__player_turn==False:

                """
                Play the minimax algorithm to find the optimum!
                """

                if self.__playerClick[1] in destination:

                    self.move.move_tiles(self.__board,self.__playerClick[0],self.__playerClick[1],-1)
                    if self.winner.check_winner(self.__board,1)!=0:
                        print("Player 2 wins:")
                        print(self.__board)
            
                    self.__player_turn = not  self.__player_turn
                    self.__playerClick =[]
                
                else:
                    print(f"{self.__playerClick[1]} is not a place to put a tile")
                    self.__playerClick.pop()
                    pass
            else:
                pass


            
 
    def main_loop(self):

        while self.__running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running =False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.game_board.reset_game()
                        self.__init__(self.game_board, self.move, self.winner,self.view)
                        print("Resetting")


                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x,y = self.__get_mouse_coordinate(pos)
                    self.__play2(x,y)
            
            self.view.draw_board(self.__screen, self.__board)
            pygame.display.update()
            self.view.clock.tick(50)
            
            
                       
                    












