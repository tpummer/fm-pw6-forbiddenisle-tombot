import gameBoard as b
import direction as d
import sys

class gameBot(object):
    def __init__(self):
        self.field = b.field(0,0,'#')
        pass

    def setField(self, field):
        self.field = field

    def getField(self):
        return self.field

    def go(self, board, direction):
        field = self.getField()
        newPosition = b.newPosition((field.getX(),field.getY()),direction)
        newField = board.getField(newPosition[0],newPosition[1])
        self.setField(newField)

    #TODO TEST
    def dry(self, board, direction):
        field = self.getField()
        dryPosition = b.newPosition((field.getX(),field.getY()),direction)
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
