class Player:
    def __init__(self, numRounds, player_number):
        self.cards = list(range(numRounds))
        self.points = 0
        self.player_number = player_number


    def checkCard(self, cardNum):
        if cardNum in self.cards:
            self.cards.remove(cardNum)
            return True
        else:
            return False

    def addPoints(self, numPoints):
        self.points += numPoints

    def getPoints(self):
        return self.points

    def printCards(self):
        print(self.cards)



