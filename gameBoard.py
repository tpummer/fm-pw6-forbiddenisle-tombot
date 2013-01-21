#fm-pw6-forbiddenisle aka TomBot - Bot for the Freies Magazin 6th programming challenge
#    Copyright (C) 2013  Thomas Pummer
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import direction as d

class field(object):
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.floodCount = 0
        self.value = value

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getFloodCount(self):
        return self.floodCount

    def setFloodCount(self, floodCount):
        self.floodCount = floodCount

class gameBoard(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fields = [[field(j,i,"#") for i in range(int(y))] for j in range(int(x))]

    def setField(self, x, y, value):
        self.fields[x][y].setValue(value)

    def getField(self, x, y):
        return self.fields[x][y]

    def getNeighbour(self, field, direction):
        newPos = newPosition((field.getX(),field.getY()),direction)
        newField = None
        if(self.isValidField(newPos)):
            newField = self.getField(newPos[0],newPos[1])
        return newField
        

    def floodField(self,x,y):
        field = self.getField(x,y)
        if(field.getValue() == '#'):
            self.setField(x,y,'o')
        elif(field.getValue() == 'o'):
            self.setField(x,y,'.')
        elif(field.getValue() == '.'):
            pass
        self.calcNeighbourFlood(x,y)

    def calcNeighbourFlood(self,x,y):
        field = self.getField(x,y)
        field.setFloodCount(self.calcFloodCount(self.getField(x,y)))
        #NORTH
        northPos = newPosition((x,y),d.direction.NORTH)
        if(self.isValidField(northPos)):
            northField = self.getField(northPos[0],northPos[1])
            northField.setFloodCount(self.calcFloodCount(northField))
        #SOUTH
        southPos = newPosition((x,y),d.direction.SOUTH)
        if(self.isValidField(southPos)):
            southField = self.getField(southPos[0],southPos[1])
            southField.setFloodCount(self.calcFloodCount(southField))
        #WEST
        westPos = newPosition((x,y),d.direction.WEST)
        if(self.isValidField(westPos)):
            westField = self.getField(westPos[0],westPos[1])
            westField.setFloodCount(self.calcFloodCount(westField))
        #EAST
        eastPos = newPosition((x,y),d.direction.EAST)
        if(self.isValidField(eastPos)):
            eastField = self.getField(eastPos[0],eastPos[1])
            eastField.setFloodCount(self.calcFloodCount(eastField))
        

    def dry(self,x,y):
        if(self.getField(x,y).getValue() == '#'):
            pass
        elif(self.getField(x,y).getValue() == 'o'):
            self.setField(x,y,'#')
        elif(self.getField(x,y).getValue() == '.'):
            pass
        self.calcNeighbourFlood(x,y)

    def updateFloodCount(self):
        for i in range(self.x):
            for j in range(self.y):
                self.fields[i][j].setFloodCount(self.calcFloodCount(self.fields[i][j]))

    def calcFloodCount(self, field):
        floodCount = 0
        #eigene feld
        if(field.getValue() == 'o'):
            floodCount = 1
        floodCount = self.calcFloodCountDirection(field, d.direction.NORTH, floodCount)
        floodCount = self.calcFloodCountDirection(field, d.direction.EAST, floodCount)
        floodCount = self.calcFloodCountDirection(field, d.direction.SOUTH, floodCount)
        floodCount = self.calcFloodCountDirection(field, d.direction.WEST, floodCount)
        return floodCount

    def calcFloodCountDirection(self, field, direction, oldCount):
        newCoordinates = newPosition((field.getX(), field.getY()), direction)
        count = oldCount
        if(self.isValidField(newCoordinates)):
            field = self.getField(newCoordinates[0], newCoordinates[1])
            if(field.getValue() == 'o'):
                count = oldCount + 1
        return count

    def isValidField(self, coordinates):
        #x
        if(coordinates[0] < 0 or coordinates[0] >= self.x):
            return False
        #y
        if(coordinates[1] < 0 or coordinates[1] >= self.y):
            return False
        return True
        

def newPosition(oldPosition, direction):
    result = list(oldPosition)
    if(direction == d.direction.NORTH):
        result[1] = result[1] -1
    elif(direction == d.direction.EAST):
        result[0] = result[0] +1
    elif(direction == d.direction.SOUTH):
        result[1] = result[1] +1
    elif(direction == d.direction.WEST):
        result[0] = result[0] -1
    elif(direction == d.direction.CURRENT):
        result = result

    return tuple(result)
