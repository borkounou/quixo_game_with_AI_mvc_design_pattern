from constants import DIMENSION,INDEX_LAST_COL,INDEX_LAST_ROW ,SQ_SIZE,IMAGE_SIZE




class Board:
    def __init__(self):
        self.board =self.__create_board()
        self.mark_squares = 0
        self.cross_turn= True
        self.sq_selected = ()
        self.player_click = []
        self.running = True
        self.start_game = False

    def __create_board(self):
        return [[0 for col in range(DIMENSION)] for row in range(DIMENSION)]
    

    def gameover(self):
        self.running = False

    def reset_game(self):
        self.__init__() 

    def next_turn(self, player_turn):
        return 1 if player_turn else -1

    def start_player(self, x,y):
        position = [(1,2),(3,2)]
        if (x,y) in position:
            if (x,y)==position[0]: self.cross_turn = True
            if (x,y)==position[1]: self.cross_turn = False
           
        return self.cross_turn



    def get_mouse_coordinate(self, pos):
        x = int((pos[0]-SQ_SIZE)/IMAGE_SIZE)
        y = int((pos[1]-SQ_SIZE)/IMAGE_SIZE)
        if x<0:x=0
        if x>4: x=4
        if y<0: y=0
        if y>4: y=4
        return x,y




    def get_possibles_destinations(self, pos_end):
        destinations = []
        (x,y) = pos_end
        if x == 0 or x == INDEX_LAST_ROW:
            if y != 0:
                destinations.append((x, 0))
            if y != INDEX_LAST_COL:
                destinations.append((x, INDEX_LAST_COL))
            opposite = 0 if x == INDEX_LAST_ROW else INDEX_LAST_ROW
            destinations.append((opposite, y))

        if (y == 0 or y == INDEX_LAST_COL) and (x != 0 and x != INDEX_LAST_ROW):
            if x != 0:
                destinations.append((0, y))
            if x != INDEX_LAST_ROW:
                destinations.append((INDEX_LAST_COL, y))
            opposite = 0 if y == INDEX_LAST_COL else INDEX_LAST_COL
            destinations.append((x, opposite))

        return destinations