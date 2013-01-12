class gameBoard(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fields = [["." for i in range(int(y))] for j in range(int(x))]

    def setField(self, x, y, value):
        self.fields[x][y] = value

    def getField(self, x, y):
        return self.fields[x][y]
