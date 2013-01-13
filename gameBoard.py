import direction as d

class gameBoard(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fields = [["#" for i in range(int(y))] for j in range(int(x))]

    def setField(self, x, y, value):
        self.fields[x][y] = value

    def getField(self, x, y):
        return self.fields[x][y]

    def floodField(self,x,y):
        if(self.getField(x,y) == '#'):
            self.setField(x,y,'o')
        elif(self.getField(x,y) == 'o'):
            self.setField(x,y,'.')
        elif(self.getField(x,y) == '.'):
            pass

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
