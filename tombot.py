#!/usr/bin/env python

import os, sys, string

def main(argv):

    runningGame = True;
    gameBoard = 1;

    while(runningGame):
        input = raw_input();

        if( input == 'END'):
                runningGame = False;
        elif(input.startswith('GAMEBOARDSTART')):
             gameBoard = readGameBoard(input);
        elif(input.startswith('ROUND')):
             #TODO make3Moves(gameBoard, input);
        elif(input.startswith('INCRFLOOD')):
             print "bingo3";
        elif(input.startswith('FLOOD')):
             print "bingo4";
        
        print input;

    print "The End of the Game";

def readGameBoard(startline):
    readBoard = True

    indexOfSpace = startline.index(' ');
    indexOfSemikolon = startline.index(',');

    xGameBoard = int(startline[indexOfSpace+1:indexOfSemikolon])
    yGameBoard = int(startline[indexOfSemikolon+1:])

    gameBoard = [["." for i in range(int(xGameBoard))] for j in range(int(yGameBoard))]

    #read y zeilen mit x zeichen
    y = 0
    while(readBoard):
        input = raw_input();
        
        if(input == 'GAMEBOARDEND'):
            readBoard = False;
        else:
            for x in range(0,xGameBoard):
                gameBoard[x][y] = input[x:x+1]

        y = y + 1

    
    return gameBoard
    

if __name__ == "__main__":
    main(sys.argv[1:])
