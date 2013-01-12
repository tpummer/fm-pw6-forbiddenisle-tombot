import gameBoard

class game(object):
    def __init__(self, inputReader):
        self.inputReader = inputReader
        self.gameBoard = 1

    def run(self):
        runningGame = True

        while(runningGame):
            input = self.inputReader.read();

            if( input == 'END'):
                    runningGame = False;
            elif(input.startswith('GAMEBOARDSTART')):
                 self.gameBoard = self.readGameBoard(input);
            elif(input.startswith('ROUND')):
                print "bingo2";
                 #TODO make3Moves(gameBoard, input);
            elif(input.startswith('INCRFLOOD')):
                 print "bingo3";
            elif(input.startswith('FLOOD')):
                 print "bingo4";

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
            input = self.inputReader.read();
            
            if(input == 'GAMEBOARDEND'):
                readBoard = False;
            else:
                for y in range(0,yGameBoard):
                    board.setField(x,y,input[y:y+1])

            x = x + 1

        
        return board
