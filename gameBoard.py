import direction as d

class field(object):
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
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

class gameBoard(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fields = [[field(j,i,"#") for i in range(int(y))] for j in range(int(x))]

    def setField(self, x, y, value):
        self.fields[x][y].setValue(value)

    def getField(self, x, y):
        return self.fields[x][y]

    def floodField(self,x,y):
        if(self.getField(x,y).getValue() == '#'):
            self.setField(x,y,'o')
        elif(self.getField(x,y).getValue() == 'o'):
            self.setField(x,y,'.')
        elif(self.getField(x,y).getValue() == '.'):
            pass

    def dry(self,x,y):
        if(self.getField(x,y).getValue() == '#'):
            pass
        elif(self.getField(x,y).getValue() == 'o'):
            self.setField(x,y,'#')
        elif(self.getField(x,y).getValue() == '.'):
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
