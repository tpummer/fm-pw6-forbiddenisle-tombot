import gameBoard as b

class gameBot(object):
    def __init__(self):
        self.position = (0,0)

    def setPosition(self, x,y):
        self.position = (x,y)

    def getPosition(self):
        return self.position

    def go(self, direction):
        oldPosition = self.getPosition()
        newPosition = b.newPosition(oldPosition,direction)
        self.setPosition(newPosition[0],newPosition[1])

    def dry(self, board, direction):
        position = self.getPosition()
        dryPosition = b.newPosition(position,direction)
        board.dry(dryPosition[0],dryPosition[1])
