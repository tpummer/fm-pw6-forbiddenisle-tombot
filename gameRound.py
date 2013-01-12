class gameRound(object):
    def __init__(self):
        self.round = 1

    def nextRound(self):
        self.round = self.round + 1

    def setRound(self, r):
        self.round = r

    def getRound(self):
        return self.round
