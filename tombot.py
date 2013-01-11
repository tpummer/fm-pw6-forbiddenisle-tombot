#!/usr/bin/env python

import os, sys, string

def main(argv):

    runningGame = True;

    while(runningGame):
        input = raw_input();

        if( input == 'END'):
                runningGame = False;
        elif(input.startswith('GAMEBOARDSTART')):
             readGameBoard();
        elif(input.startswith('ROUND')):
             print "bingo2";
        elif(input.startswith('INCRFLOOD')):
             print "bingo3";
        elif(input.startswith('FLOOD')):
             print "bingo4";
        
        print input;

    print "The End of the Game";

def readGameBoard():
    readBoard = True

    while(readBoard):
        input = raw_input();
        if(input == 'GAMEBOARDEND'):
            readBoard = False;
            
    print "Done!";
    

if __name__ == "__main__":
    main(sys.argv[1:])
