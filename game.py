import gameBoard
import gameRound as r
import gameBot as bot
import inputReader as reader

class game(object):
    def __init__(self, inputReader):
        self.inputReader = inputReader
        self.gameBoard = gameBoard.gameBoard(1,1)
        self.round = r.gameRound()
        self.bot = bot.gameBot()
        self.flood = 0

    def run(self):
        runningGame = True

        while(runningGame):
            inputText = self.inputReader.read();

            if( inputText == 'END'):
                runningGame = False
            elif(inputText.startswith('GAMEBOARDSTART')):
                self.gameBoard = self.readGameBoard(inputText)
            elif(inputText.startswith('ROUND')):
                self.reportRound(inputText, self.round, self.bot)
                self.bot.makeTurn(self.gameBoard)
            elif(inputText.startswith('INCRFLOOD')):
                self.incrFlood(inputText);
            elif(inputText.startswith('FLOOD')):
                self.floodField(inputText);

    def floodField(self,inputText):
        parts = inputText.split(' ')
        coordinates = reader.coordinateTextToTuple(parts[1])
        self.gameBoard.floodField(coordinates[0],coordinates[1])

    def incrFlood(self,inputText):
        additionalValue = int(inputText.split(' ')[1])
        self.flood = self.flood + additionalValue
        pass

    def reportRound(self, inputText, r, bot):
        parts = inputText.split(' ')
        r.setRound(int(parts[1]))
        coordinates = reader.coordinateTextToTuple(parts[2])
        bot.setField(self.gameBoard.getField(coordinates[0],coordinates[1]))

    def readGameBoard(self,startline):
        readBoard = True

        indexOfSpace = startline.index(' ');
        indexOfSemikolon = startline.index(',');

        xGameBoard = int(startline[indexOfSpace+1:indexOfSemikolon])
        yGameBoard = int(startline[indexOfSemikolon+1:])

        board = gameBoard.gameBoard(xGameBoard,yGameBoard)

        #read y zeilen mit x zeichen
        y = 0
        while(readBoard):
            inputText = self.inputReader.read();
            
            if(inputText == 'GAMEBOARDEND'):
                readBoard = False;
            else:
                for x in range(0,xGameBoard):
                    board.setField(x,y,inputText[x:x+1])

            y = y + 1
        
        return board

    def getFlood(self):
        return self.flood

    def getGameBoard(self):
        return self.gameBoard
