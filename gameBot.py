class gameBot(object):
    def __init__(self):
        self.position = (0,0)

    def setPosition(self, x,y):
        self.position = (x,y)

    def getPosition(self):
        return self.position
