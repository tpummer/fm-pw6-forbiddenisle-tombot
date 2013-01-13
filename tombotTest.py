#!/usr/bin/env python

import os, sys, string
import fakeInputReader as f
import game as g
import random
import unittest
import gameBoard
import gameRound
import gameBot
import direction as d

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    ############### GAMEBOT ###############

    def test_gameBotGetPosition(self):
        bot = gameBot.gameBot()
        self.assertEquals(bot.getPosition()[0],0)
        self.assertEquals(bot.getPosition()[1],0)
        bot.setPosition(1,1)
        self.assertEquals(bot.getPosition()[0],1)
        self.assertEquals(bot.getPosition()[1],1)

    def test_gameBotGo(self):
        bot = gameBot.gameBot()
        bot.setPosition(1,1)
        self.assertEquals(bot.getPosition()[0],1)
        self.assertEquals(bot.getPosition()[1],1)
        bot.go(d.direction.NORTH)
        self.assertEquals(bot.getPosition()[0],1)
        self.assertEquals(bot.getPosition()[1],0)
        bot.go(d.direction.CURRENT)
        self.assertEquals(bot.getPosition()[0],1)
        self.assertEquals(bot.getPosition()[1],0)

    def test_gameBotDry(self):
        bot = gameBot.gameBot()
        board = gameBoard.gameBoard(1,1)
        self.assertEqual(board.getField(0,0), '#')
        bot.dry(board, d.direction.CURRENT)
        self.assertEqual(board.getField(0,0), '#')
        board.setField(0,0,'o')
        self.assertEqual(board.getField(0,0), 'o')
        bot.dry(board, d.direction.CURRENT)
        self.assertEqual(board.getField(0,0), '#')
        board.setField(0,0,'.')
        self.assertEqual(board.getField(0,0), '.')
        bot.dry(board, d.direction.CURRENT)
        self.assertEqual(board.getField(0,0), '.')

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

    def test_gameBoardDry(self):
        board = gameBoard.gameBoard(1,1)
        self.assertEqual(board.getField(0,0), '#')
        board.dry(0,0)
        self.assertEqual(board.getField(0,0), '#')
        board.setField(0,0,'o')
        self.assertEqual(board.getField(0,0), 'o')
        board.dry(0,0)
        self.assertEqual(board.getField(0,0), '#')
        board.setField(0,0,'.')
        self.assertEqual(board.getField(0,0), '.')
        board.dry(0,0)
        self.assertEqual(board.getField(0,0), '.')

    def test_gameBoardFloodField(self):
        board = gameBoard.gameBoard(1,1)
        self.assertEqual(board.getField(0,0), '#')
        board.floodField(0,0)
        self.assertEqual(board.getField(0,0), 'o')
        board.floodField(0,0)
        self.assertEqual(board.getField(0,0), '.')
        board.floodField(0,0)
        self.assertEqual(board.getField(0,0), '.')
        
    def test_gameBoardNewPosition(self):
        board = gameBoard.gameBoard(3,3)
        self.assertEqual(gameBoard.newPosition((1,1),d.direction.NORTH),(1,0))
        self.assertEqual(gameBoard.newPosition((1,1),d.direction.EAST),(2,1))
        self.assertEqual(gameBoard.newPosition((1,1),d.direction.SOUTH),(1,2))
        self.assertEqual(gameBoard.newPosition((1,1),d.direction.WEST),(0,1))
        self.assertEqual(gameBoard.newPosition((1,1),d.direction.CURRENT),(1,1))

    def test_gameBoardSize(self):
        board = gameBoard.gameBoard(4,10)
        self.assertEqual(len(board.fields),4)
        self.assertEqual(len(board.fields[0]),10)

    def test_gameBoardSetValue(self):
        board = gameBoard.gameBoard(2,2)
        self.assertEqual(board.getField(0,0), '#')
        self.assertEqual(board.getField(0,1), '#')
        self.assertEqual(board.getField(1,0), '#')
        self.assertEqual(board.getField(1,1), '#')
        board.setField(1,0,'!')
        self.assertEqual(board.getField(0,0), '#')
        self.assertEqual(board.getField(0,1), '#')
        self.assertEqual(board.getField(1,0), '!')
        self.assertEqual(board.getField(1,1), '#')

    def test_gameBoardSetValue(self):
        board = gameBoard.gameBoard(2,2)
        self.assertEqual(board.getField(0,0), '#')
        self.assertEqual(board.getField(0,1), '#')
        self.assertEqual(board.getField(1,0), '#')
        self.assertEqual(board.getField(1,1), '#')
        board.floodField(1,0)
        self.assertEqual(board.getField(0,0), '#')
        self.assertEqual(board.getField(0,1), '#')
        self.assertEqual(board.getField(1,0), 'o')
        self.assertEqual(board.getField(1,1), '#')
        board.floodField(1,0)
        self.assertEqual(board.getField(0,0), '#')
        self.assertEqual(board.getField(0,1), '#')
        self.assertEqual(board.getField(1,0), '.')
        self.assertEqual(board.getField(1,1), '#')
        board.floodField(1,0)
        self.assertEqual(board.getField(0,0), '#')
        self.assertEqual(board.getField(0,1), '#')
        self.assertEqual(board.getField(1,0), '.')
        self.assertEqual(board.getField(1,1), '#')

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

    def test_gameReportRound(self):
        test = []
        app = g.game(f.fakeInputReader(test))
        r = gameRound.gameRound()
        self.assertEqual(r.getRound(),1)
        bot = gameBot.gameBot()
        self.assertEquals(bot.getPosition()[0],0)
        self.assertEquals(bot.getPosition()[1],0)
        inputText = "ROUND 3 13,21"
        app.reportRound(inputText,r,bot)
        self.assertEqual(r.getRound(),3)
        self.assertEquals(bot.getPosition()[0],13)
        self.assertEquals(bot.getPosition()[1],21)

    def test_gameFlood(self):
        testBoard = ["GAMEBOARDSTART 1,1","#", "GAMEBOARDEND", "END"]
        app = g.game(f.fakeInputReader(testBoard))
        app.run()
        self.assertEqual(app.getGameBoard().getField(0,0),"#")
        app.floodField("FLOOD 0,0")
        self.assertEqual(app.getGameBoard().getField(0,0),"o")
        app.floodField("FLOOD 0,0")
        self.assertEqual(app.getGameBoard().getField(0,0),".")
        app.floodField("FLOOD 0,0")
        self.assertEqual(app.getGameBoard().getField(0,0),".")

    def test_gameIncrFlood(self):
        test = []
        app = g.game(f.fakeInputReader(test))
        self.assertEquals(app.getFlood(),0)
        app.incrFlood('INCRFLOOD 3')
        self.assertEquals(app.getFlood(),3)
        app.incrFlood('INCRFLOOD 0')
        self.assertEquals(app.getFlood(),3)
        app.incrFlood('INCRFLOOD 1')
        self.assertEquals(app.getFlood(),4)

    def test_gameReadGameBoard(self):
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
