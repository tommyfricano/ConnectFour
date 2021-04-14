import random
import numpy as np

class Game:
    def __init__(self ):
        self.row_count = 6
        self.column_count = 7
        #self.game_count = game_count
        self.board = np.zeros((self.row_count,self.column_count))
    
    def create_game(self):
        return np.flip(self.board, 0)

    def open_spot(self, column):
        return self.board[self.row_count-1][column] == 0

    def play(self, row, col, move):
        self.board[row][col] = move

    def check_win(self, move):
                                                                    #checks vertical
        for c in range(self.column_count):
            for r in range(self.row_count):
                if self.board[r][c] == move and self.board[r+1][c] and self.board[r+2][c] == move and self.board[r+3][c] == move:
                    return True
                                                                    #checks horizontal
        for c in range(self.column_count):
            for r in range(self.row_count):
                if self.board[r][c] == move and self.board[r][c+1] and self.board[r][c+2] == move and self.board[r][c+3] == move:
                    return True   
                                                                    #checks left to right diaganol 
        for c in range(self.column_count):
            for r in range(self.row_count):
                if self.board[r][c] == move and self.board[r+1][c+1] and self.board[r+2][c+2] == move and self.board[r+3][c+3] == move:
                    return True
        
        for c in range(self.column_count):
            for r in range(self.row_count):
                if self.board[r][c] == move and self.board[r-1][c+1] and self.board[r-2][c+2] == move and self.board[r-3][c+3] == move:
                    return True

#Setup player(s)
print("Connect Four!" + "\n(Press enter when ready to play!)")
input()
#num_games = input("How many games do you want to play: \n1)One game \n2)Best of three \n3)Best of five \n")
finished = False
turn = 0 

connect = Game(num_games)
connect.create_game()

while not finished:
    if turn % 2 == 0:
        current_player = "player1"
        piece = "x"
    else:
        current_player = "player2"
        piece = "o"
    if connect.open_spot(int(input("Where do you want to drop? (1-6)"))) == True:
        connect.play()