class Game:
    def __init__(self, num_players, num_cards):
        self.num_players = num_players
        self.num_cards = num_cards

    def play (self):
        for roundNum in range(self.num_cards):
            cardsPicked = []
            for playerNum in range(self.num_players):
                print("Player " + playerNum + ", pick a card.")
                cardIsAvailable = False
                while cardIsAvailable == False:
                    print("Here are the cards you can pick:")
                    print(self.players[playerNum].cards)
                    pickedCard = int(input())
                    cardIsAvailable = self.players[playerNum].checkCard()
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
            else:
                for playerNum in range(self.num_players):
                    if cardsPicked[playerNum] == highestRoundValue:
                        self.players[playerNum].addPoints(2)


print("Welcome to the pyramid game!")
print("How many players are there? (Must be at least 2)")
num_players = int(input())
print("How many cards do you want each player to have?")
num_cards = int(input())
game = Game(num_players, num_cards)
game.play()
