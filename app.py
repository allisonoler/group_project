from player import Player

class Game:
    def __init__(self, num_players, num_cards):
        self.num_players = num_players
        self.num_cards = num_cards
        self.players = []
        for i in range(num_players):
            player = Player(num_cards, i + 1)
            self.players.append(player)

    def play (self):
        print("playing game")
    def print_scores (self):
        print("printing scores here")


print("Welcome to the pyramid game!")
print("How many players are there? (Must be at least 2)")
num_players = int(input())
print("How many cards do you want each player to have?")
num_cards = int(input())
game = Game(num_players, num_cards)
game.play()
