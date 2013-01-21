import gameBoard as b
import direction as d
import sys
from random import randrange

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

    def dry(self, board, direction):
        field = self.getField()
        dryPosition = b.newPosition((field.getX(),field.getY()),direction)
        board.dry(dryPosition[0],dryPosition[1])

    def calcNextTurn(self, board, turn):
        bestMove = d.direction.CURRENT
        bestMoveCount = self.getField().getFloodCount()
        if(bestMoveCount == 0):
            turn = turn -1

        northNeighbour = board.getNeighbour(self.getField(),d.direction.NORTH)
        if(northNeighbour is not None and northNeighbour.getValue() is not '.'):
            if(northNeighbour.getFloodCount() - turn > bestMoveCount):
                bestMoveCount = northNeighbour.getFloodCount()
                bestMove = d.direction.NORTH

        westNeighbour = board.getNeighbour(self.getField(),d.direction.WEST)    
        if(westNeighbour is not None and westNeighbour.getValue() is not '.'):
            if(westNeighbour.getFloodCount() - turn > bestMoveCount):
                bestMoveCount = westNeighbour.getFloodCount()
                bestMove = d.direction.WEST

        southNeighbour = board.getNeighbour(self.getField(),d.direction.SOUTH)    
        if(southNeighbour is not None and southNeighbour.getValue() is not '.'):
            if(southNeighbour.getFloodCount() - turn > bestMoveCount):
                bestMoveCount = southNeighbour.getFloodCount()
                bestMove = d.direction.SOUTH

        eastNeighbour = board.getNeighbour(self.getField(),d.direction.EAST)    
        if(eastNeighbour is not None and eastNeighbour.getValue() is not '.'):
            if(eastNeighbour.getFloodCount() - turn > bestMoveCount):
                bestMoveCount = eastNeighbour.getFloodCount()
                bestMove = d.direction.EAST

        return bestMove

    ## NOUNITTEST only executes strategy
    def makeTurn(self, board):
        #self.drySimple(board)
        self.tryCleanmost(board)

    def drySimple(self,board):
        print "DRY CURRENT"
        sys.stdout.flush()
        self.dry(board, d.direction.CURRENT)
        print "DRY CURRENT"
        sys.stdout.flush()
        self.dry(board, d.direction.CURRENT)
        print "DRY CURRENT"
        sys.stdout.flush()
        self.dry(board, d.direction.CURRENT)
        
    def tryCleanmost(self,board):
        turns = 0
        nextField = False
        while(turns < 3):
            nextTurn = self.calcNextTurn(board, turns + 1)

            if(nextTurn == d.direction.CURRENT and not nextField):
                if(self.getField().getValue() == 'o'):
                    print "DRY CURRENT"
                    sys.stdout.flush()
                    self.dry(board, d.direction.CURRENT)
                    turns = turns + 1


                while(turns < 3 and not nextField and self.calcNextTurn(board, turns + 1) == d.direction.CURRENT):
                    northNeighbour = board.getNeighbour(self.getField(),d.direction.NORTH)
                    eastNeighbour = board.getNeighbour(self.getField(),d.direction.EAST)
                    southNeighbour = board.getNeighbour(self.getField(),d.direction.SOUTH)
                    westNeighbour = board.getNeighbour(self.getField(),d.direction.WEST)
                    
                    if(northNeighbour is not None and northNeighbour.getValue() == 'o'):
                        print "DRY NORTH"
                        sys.stdout.flush()
                        self.dry(board, d.direction.NORTH)
                        turns = turns + 1
                    elif(eastNeighbour is not None and eastNeighbour.getValue() == 'o'):
                        print "DRY EAST"
                        sys.stdout.flush()
                        self.dry(board, d.direction.EAST)
                        turns = turns + 1
                    elif(southNeighbour is not None and southNeighbour.getValue() == 'o'):
                        print "DRY SOUTH"
                        sys.stdout.flush()
                        self.dry(board, d.direction.SOUTH)
                        turns = turns + 1
                    elif(westNeighbour is not None and westNeighbour.getValue() == 'o'):
                        print "DRY WEST"
                        sys.stdout.flush()
                        self.dry(board, d.direction.WEST)
                        turns = turns + 1
                    else:
                        nextField = True
            else:
                if(nextTurn == d.direction.NORTH):
                    print "GO NORTH"
                elif(nextTurn == d.direction.EAST):
                    print "GO EAST"
                elif(nextTurn == d.direction.SOUTH):
                    print "GO SOUTH"
                elif(nextTurn == d.direction.WEST):
                    print "GO WEST"
                else:
                    gone = False
                    while(not gone):
                        newDirection = randrange(4)
                        
                        northNeighbour = board.getNeighbour(self.getField(),d.direction.NORTH)
                        eastNeighbour = board.getNeighbour(self.getField(),d.direction.EAST)
                        southNeighbour = board.getNeighbour(self.getField(),d.direction.SOUTH)
                        westNeighbour = board.getNeighbour(self.getField(),d.direction.WEST)
                        
                        if(newDirection == 0 and northNeighbour is not None and northNeighbour.getValue() is not '.'):
                            print "GO NORTH"
                            nextTurn = d.direction.NORTH
                            gone = True
                        elif(newDirection == 1 and eastNeighbour is not None and eastNeighbour.getValue() is not '.'):
                            print "GO EAST"
                            nextTurn = d.direction.EAST
                            gone = True
                        elif(newDirection == 2 and southNeighbour is not None and southNeighbour.getValue() is not '.'):
                            print "GO SOUTH"
                            nextTurn = d.direction.SOUTH
                            gone = True
                        elif(newDirection == 3 and westNeighbour is not None and westNeighbour.getValue() is not '.'):
                            print "GO WEST"
                            nextTurn = d.direction.WEST
                            gone = True

                        if(westNeighbour is not None and westNeighbour.getValue() is '.'
                           and southNeighbour is not None and southNeighbour.getValue() is '.'
                           and eastNeighbour is not None and eastNeighbour.getValue() is '.'
                           and northNeighbour is not None and northNeighbour.getValue() is '.'):
                            print "GO CURRENT"
                            nextTurn = d.direction.CURRENT
                            gone = True

                        if((westNeighbour is None or neighbourIsNotAccessable(westNeighbour))
                           and (westNeighbour is None or neighbourIsNotAccessable(westNeighbour))
                           and (westNeighbour is None or neighbourIsNotAccessable(westNeighbour))
                           and (westNeighbour is None or neighbourIsNotAccessable(westNeighbour))):
                            print "GO CURRENT"
                            nextTurn = d.direction.CURRENT
                            gone = True
                self.go(board,nextTurn)
                sys.stdout.flush()
                turns = turns + 1
                nextField = False
def neighbourIsNotAccessable(neighbourField):
    if(neighbourField is not None and neighbourField.getValue() is '.'):
        return True
    else:
        return False
        pass
