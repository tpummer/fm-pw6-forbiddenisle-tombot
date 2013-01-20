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
        #print "curr " + str(self.getField().getX()) + " " + str(self.getField().getY())
        bestMoveCount = self.getField().getFloodCount()
        if(bestMoveCount == 0):
            turn = turn -1
        #print bestMoveCount

        northNeighbour = board.getNeighbour(self.getField(),d.direction.NORTH)
        if(northNeighbour is not None and northNeighbour.getValue() is not '.'):
            if(northNeighbour.getFloodCount() - turn > bestMoveCount):
                bestMoveCount = northNeighbour.getFloodCount()
                bestMove = d.direction.NORTH
                #print "north"

        westNeighbour = board.getNeighbour(self.getField(),d.direction.WEST)    
        if(westNeighbour is not None and westNeighbour.getValue() is not '.'):
            if(westNeighbour.getFloodCount() - turn > bestMoveCount):
                bestMoveCount = westNeighbour.getFloodCount()
                bestMove = d.direction.WEST
                #print "west"

        southNeighbour = board.getNeighbour(self.getField(),d.direction.SOUTH)    
        if(southNeighbour is not None and southNeighbour.getValue() is not '.'):
            if(southNeighbour.getFloodCount() - turn > bestMoveCount):
                bestMoveCount = southNeighbour.getFloodCount()
                bestMove = d.direction.SOUTH
                #print "south"

        eastNeighbour = board.getNeighbour(self.getField(),d.direction.EAST)    
        if(eastNeighbour is not None and eastNeighbour.getValue() is not '.'):
            if(eastNeighbour.getFloodCount() - turn > bestMoveCount):
                bestMoveCount = eastNeighbour.getFloodCount()
                bestMove = d.direction.EAST
                #print "east"

        return bestMove

    ## NOUNITTEST only executes strategy
    def makeTurn(self, board):
        #print"AHAHAHAH"
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
            #print "next: "+nextTurn

            if(nextTurn == d.direction.CURRENT and not nextField):
                #print "in"
                if(self.getField().getValue() == 'o'):
                    print "DRY CURRENT"
                    sys.stdout.flush()
                    self.dry(board, d.direction.CURRENT)
                    turns = turns + 1


                while(turns < 3 and not nextField and self.calcNextTurn(board, turns + 1) == d.direction.CURRENT):
                    #print "while"
                    northNeighbour = board.getNeighbour(self.getField(),d.direction.NORTH)
                    #if(northNeighbour is not None):
                    #    print "north"
                    eastNeighbour = board.getNeighbour(self.getField(),d.direction.EAST)
                    #if(eastNeighbour is not None):
                    #    print "east" + str(eastNeighbour.getX()) +" "+str(eastNeighbour.getY())
                    #    print board.getNeighbour(self.getField(),d.direction.EAST).getValue()
                    southNeighbour = board.getNeighbour(self.getField(),d.direction.SOUTH)
                    #if(southNeighbour is not None):
                    #    print "south"
                    westNeighbour = board.getNeighbour(self.getField(),d.direction.WEST)
                    #if(westNeighbour is not None):
                    #    print "west"
                    
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
                        #print "next"
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
                    #print "else"
                    gone = False
                    while(not gone):
                        newDirection = randrange(4)
                        
                        northNeighbour = board.getNeighbour(self.getField(),d.direction.NORTH)
                        eastNeighbour = board.getNeighbour(self.getField(),d.direction.EAST)
                        southNeighbour = board.getNeighbour(self.getField(),d.direction.SOUTH)
                        westNeighbour = board.getNeighbour(self.getField(),d.direction.WEST)
                        #if(westNeighbour is '.'):
                        #    print "bla"
                        #if(westNeighbour.getValue() is not '.'):
                        #    print "bla2"

                        #print newDirection
                        
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
                self.go(board,nextTurn)
                #print str(self.getField().getX()) + " " + str(self.getField().getY())
                sys.stdout.flush()
                turns = turns + 1
                nextField = False
