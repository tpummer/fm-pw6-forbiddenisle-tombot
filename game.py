import gameBoard
import gameRound as r
import gameBot as bot

class game(object):
    def __init__(self, inputReader):
        self.inputReader = inputReader
        self.gameBoard = 1
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
                reportRound(inputText, self.round, self.bot)
                 #TODO make3Moves(gameBoard, input);
            elif(inputText.startswith('INCRFLOOD')):
                incrFlood(inputText);
            elif(inputText.startswith('FLOOD')):
                print "bingo4";

    def incrFlood(self,inputText):
        additionalValue = int(inputText.split(' ')[1])
        self.flood = self.flood + additionalValue
        pass

    def reportRound(self, inputText, r, bot):
        parts = inputText.split(' ')
        r.setRound(int(parts[1]))
        coordinates = parts[2].split(',')
        bot.setPosition(int(coordinates[0]),int(coordinates[1]))

    def readGameBoard(self,startline):
        readBoard = True

        indexOfSpace = startline.index(' ');
        indexOfSemikolon = startline.index(',');

        xGameBoard = int(startline[indexOfSpace+1:indexOfSemikolon])
        yGameBoard = int(startline[indexOfSemikolon+1:])

        board = gameBoard.gameBoard(xGameBoard,yGameBoard)

        #read y zeilen mit x zeichen
        x = 0
        while(readBoard):
            inputText = self.inputReader.read();
            
            if(inputText == 'GAMEBOARDEND'):
                readBoard = False;
            else:
                for y in range(0,yGameBoard):
                    board.setField(x,y,inputText[y:y+1])

            x = x + 1

        
        return board

    def getFlood(self):
        return self.flood
