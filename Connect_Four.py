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

    def get_row(self, col):
        for i in range(self.row_count):
            if self.board[i][col] == 0:
                return i

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

connect = Game()
connect.create_game()

while not finished:
    if turn % 2 == 0:
        current_player = "player1"
        piece = 1
        print(connect.create_game())
        move = int(input("Where do you want to drop player 1? (1-6)")) -1
        if connect.open_spot(move):
            row = connect.get_row(move)
            connect.play(row, move, piece)
            print(connect.create_game())
    else:
        current_player = "player2"
        piece = 2
        move = int(input("Where do you want to drop player 2? (1-6)")) -1
        if connect.open_spot(move):
            row = connect.get_row(move)
            connect.play(row, move, piece)
    turn += 1