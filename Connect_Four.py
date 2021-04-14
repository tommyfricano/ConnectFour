import random

class Game:
    def __init__(self, player_count, game_count):
        self.player_count = player_count
        self.game_count = game_count
    
    def create_game(self):
        print("\n|  |  |  |  |  |  |  |\n|  |  |  |  |  |  |  |\n|  |  |  |  |  |  |  |\n|  |  |  |  |  |  |  |\n|  |  |  |  |  |  |  |\n|  |  |  |  |  |  |  |")


#Setup player(s)
print("Connect Four!" + "\n(Press enter when ready to play!)")
input()
num_players = input("How many players(type 1 or 2)\n") 
num_games = input("How many games do you want to play: \n1)One game \n2)Best of three \n3)Best of five \n")

new_game = Game(num_players, num_games)
new_game.create_game()

