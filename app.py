from player import Player

class Game:
    def __init__(self, num_players, num_cards):
        self.num_players = num_players
        self.num_cards = num_cards
        self.players = []
        for i in range(num_players):
            player = Player(num_cards, i + 1)
            self.players.append(player)

    def print_leaderboard(self):
        self.players.sort(key=lambda player: player.score, reverse=True)
        for place, player in enumerate(self.players, start=1):
            print("{}: Player {} {} points".format(place, player.player_number, player.points))

    def play (self):
        for roundNum in range(self.num_cards):
            cardsPicked = [-1 for x in range(self.num_players)]
            for playerNum in range(self.num_players):
                print("Player " + str(playerNum+1) + ", pick a card.")
                cardIsAvailable = False
                while cardIsAvailable == False:
                    print("Here are the cards you can pick:")
                    print(self.players[playerNum].cards)
                    pickedCard = int(input())
                    cardIsAvailable = self.players[playerNum].checkCard(pickedCard)
                    cardsPicked[playerNum] = pickedCard
            highestRoundValue = max(cardsPicked)
            numMaxPlayers = 0
            for playerNum in range (self.num_players):
                if cardsPicked[playerNum] == highestRoundValue:
                    numMaxPlayers +=1
            if numMaxPlayers >1:
                for playerNum in range(self.num_players):
                    if cardsPicked[playerNum] == highestRoundValue:
                        self.players[playerNum].addPoints(1)
                print("There was a tie, each player in the tie received one point.")
            else:
                for playerNum in range(self.num_players):
                    if cardsPicked[playerNum] == highestRoundValue:
                        self.players[playerNum].addPoints(2)
                        print("Player " + str(playerNum + 1) + " won!")
        self.print_leaderboard()


print("Welcome to the pyramid game!")
print("How many players are there? (Must be at least 2)")
num_players = int(input())
print("How many cards do you want each player to have?")
num_cards = int(input())
game = Game(num_players, num_cards)
game.play()
