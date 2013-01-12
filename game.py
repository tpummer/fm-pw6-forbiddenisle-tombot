class game(object):
    def __init__(self, inputReader):
        self.inputReader = inputReader

    def run(self):
        runningGame = True
        gameBoard = 1

        while(runningGame):
            input = self.inputReader.read();

            if( input == 'END'):
                    runningGame = False;
            elif(input.startswith('GAMEBOARDSTART')):
                 gameBoard = self.readGameBoard(input);
            elif(input.startswith('ROUND')):
                print "bingo2";
                 #TODO make3Moves(gameBoard, input);
            elif(input.startswith('INCRFLOOD')):
                 print "bingo3";
            elif(input.startswith('FLOOD')):
                 print "bingo4";

        print "The End of the Game";

    def readGameBoard(self,startline):
        readBoard = True

        indexOfSpace = startline.index(' ');
        indexOfSemikolon = startline.index(',');

        xGameBoard = int(startline[indexOfSpace+1:indexOfSemikolon])
        yGameBoard = int(startline[indexOfSemikolon+1:])

        gameBoard = [["." for i in range(int(xGameBoard))] for j in range(int(yGameBoard))]

        #read y zeilen mit x zeichen
        y = 0
        while(readBoard):
            input = self.inputReader.read();
            
            if(input == 'GAMEBOARDEND'):
                readBoard = False;
            else:
                for x in range(0,xGameBoard):
                    gameBoard[x][y] = input[x:x+1]

            y = y + 1

        
        return gameBoard
