#!/usr/bin/env python

import os, sys, string
import fakeInputReader as f
import game as g
import random
import unittest
import gameBoard
import gameRound

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    ############### GAMEROUND ###############

    def test_gameRoundNextRound(self):
        r = gameRound.gameRound()
        r.nextRound()
        r.nextRound()
        r.nextRound()
        self.assertEqual(r.getRound(),4)
        
    def test_gameRoundSetRound(self):
        matchingRound = 10
        r = gameRound.gameRound()
        r.setRound(matchingRound)
        self.assertEqual(r.getRound(),matchingRound)

    ############### GAMEBOARD ###############

    def test_gameBoardSize(self):
        board = gameBoard.gameBoard(4,10)
        self.assertEqual(len(board.fields),4)
        self.assertEqual(len(board.fields[0]),10)

    def test_gameBoardSetValue(self):
        board = gameBoard.gameBoard(2,2)
        self.assertEqual(board.getField(0,0), '.')
        self.assertEqual(board.getField(0,1), '.')
        self.assertEqual(board.getField(1,0), '.')
        self.assertEqual(board.getField(1,1), '.')
        board.setField(1,0,'!')
        self.assertEqual(board.getField(0,0), '.')
        self.assertEqual(board.getField(0,1), '.')
        self.assertEqual(board.getField(1,0), '!')
        self.assertEqual(board.getField(1,1), '.')

    ############### FAKEINPUTREADER ###############

    def test_fakeInputReaderReadLines(self):
        lines = ['123','456','789']
        reader = f.fakeInputReader(lines)
        self.assertEqual(reader.read(),'123')
        self.assertEqual(reader.read(),'456')
        self.assertEqual(reader.read(),'789')
        self.assertEqual(reader.read(),'IndexError')

    ############### GAME ###############

    ### Integration Test ###
    def test_runTillEnd(self):
        fooTillEnd = ["GAMEBOARDSTART 2,2", "oo", "oo", "GAMEBOARDEND", "END"]
        app = g.game(f.fakeInputReader(fooTillEnd))
        app.run()
        self.assertTrue(True)

    def test_readGameBoard(self):
        testBoard = ["oxf", "jlk", "GAMEBOARDEND", "END"]
        app = g.game(f.fakeInputReader(testBoard))
        board = app.readGameBoard("GAMEBOARDSTART 2,3")
        self.assertEqual(board.getField(0,0),"o")
        self.assertEqual(board.getField(0,1),"x")
        self.assertEqual(board.getField(0,2),"f")
        self.assertEqual(board.getField(1,0),"j")
        self.assertEqual(board.getField(1,1),"l")
        self.assertEqual(board.getField(1,2),"k")

if __name__ == "__main__":
    unittest.main()
