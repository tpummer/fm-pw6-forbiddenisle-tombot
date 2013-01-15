import gameBoard as b
import direction as d
import sys

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

    ## NOUNITTEST only executes strategy
    def makeTurn(self, board):
        print "DRY CURRENT"
        sys.stdout.flush()
        self.dry(board, d.direction.CURRENT)
        print "DRY CURRENT"
        sys.stdout.flush()
        self.dry(board, d.direction.CURRENT)
        print "DRY CURRENT"
        sys.stdout.flush()
        self.dry(board, d.direction.CURRENT)
