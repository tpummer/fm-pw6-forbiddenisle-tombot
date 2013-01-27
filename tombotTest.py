#!/usr/bin/env python

#fm-pw6-forbiddenisle aka TomBot - Bot for the Freies Magazin 6th programming challenge
#    Copyright (C) 2013  Thomas Pummer
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os, sys, string
import game as g
import random
import unittest
import gameBoard
import gameRound
import gameBot
import direction as d
import inputReader as reader

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    ############### GAMEBOT ###############

    def test_gameBotGetField(self):
        bot = gameBot.gameBot()
        self.assertEquals(bot.getField().getX(),0)
        self.assertEquals(bot.getField().getY(),0)
        bot.setField(gameBoard.field(1,1,'#'))
        self.assertEquals(bot.getField().getX(),1)
        self.assertEquals(bot.getField().getY(),1)

    def test_gameBotGo(self):
        bot = gameBot.gameBot()
        board = gameBoard.gameBoard(3,3)
        bot.setField(board.getField(1,1))
        self.assertEquals(bot.getField().getX(),1)
        self.assertEquals(bot.getField().getY(),1)
        bot.go(board, d.direction.NORTH)
        self.assertEquals(bot.getField().getX(),1)
        self.assertEquals(bot.getField().getY(),0)
        bot.go(board, d.direction.CURRENT)
        self.assertEquals(bot.getField().getX(),1)
        self.assertEquals(bot.getField().getY(),0)

    def test_gameBotDry(self):
        bot = gameBot.gameBot()
        board = gameBoard.gameBoard(2,2)
        bot.setField(board.getField(0,1))
        self.assertEqual(board.getField(0,1).getValue(), '#')
        bot.dry(board, d.direction.CURRENT)
        self.assertEqual(board.getField(0,1).getValue(), '#')
        board.setField(0,1,'o')
        self.assertEqual(board.getField(0,1).getValue(), 'o')
        bot.dry(board, d.direction.CURRENT)
        self.assertEqual(board.getField(0,1).getValue(), '#')
        board.setField(0,1,'.')
        self.assertEqual(board.getField(0,1).getValue(), '.')
        bot.dry(board, d.direction.CURRENT)
        self.assertEqual(board.getField(0,1).getValue(), '.')

    def test_gameBotCalcNextTurn(self):
        board = gameBoard.gameBoard(3,3)
        board.setField(1,0,'o')
        board.setField(0,1,'o')
        board.setField(1,2,'o')
        board.setField(2,1,'.')
        board.updateFloodCount()
        bot = gameBot.gameBot()
        bot.setField(board.getField(1,1))
        self.assertEquals(bot.calcNextTurn(board, 0),d.direction.CURRENT)
        bot.setField(board.getField(1,2))
        self.assertEquals(bot.calcNextTurn(board, 0),d.direction.NORTH)
        bot.setField(board.getField(2,2))
        self.assertEquals(bot.calcNextTurn(board, 0),d.direction.CURRENT)

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
        self.assertEqual(board.getField(0,0).getValue(), '#')
        board.dry(0,0)
        self.assertEqual(board.getField(0,0).getValue(), '#')
        board.setField(0,0,'o')
        self.assertEqual(board.getField(0,0).getValue(), 'o')
        board.dry(0,0)
        self.assertEqual(board.getField(0,0).getValue(), '#')
        board.setField(0,0,'.')
        self.assertEqual(board.getField(0,0).getValue(), '.')
        board.dry(0,0)
        self.assertEqual(board.getField(0,0).getValue(), '.')

    def test_gameBoardFloodField(self):
        board = gameBoard.gameBoard(1,1)
        self.assertEqual(board.getField(0,0).getValue(), '#')
        board.floodField(0,0)
        self.assertEqual(board.getField(0,0).getValue(), 'o')
        board.floodField(0,0)
        self.assertEqual(board.getField(0,0).getValue(), '.')
        board.floodField(0,0)
        self.assertEqual(board.getField(0,0).getValue(), '.')
        
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
        self.assertEqual(board.getField(0,0).getValue(), '#')
        self.assertEqual(board.getField(0,1).getValue(), '#')
        self.assertEqual(board.getField(1,0).getValue(), '#')
        self.assertEqual(board.getField(1,1).getValue(), '#')
        board.setField(1,0,'!')
        self.assertEqual(board.getField(0,0).getValue(), '#')
        self.assertEqual(board.getField(0,1).getValue(), '#')
        self.assertEqual(board.getField(1,0).getValue(), '!')
        self.assertEqual(board.getField(1,1).getValue(), '#')

    def test_gameBoardSetValue(self):
        board = gameBoard.gameBoard(2,2)
        self.assertEqual(board.getField(0,0).getValue(), '#')
        self.assertEqual(board.getField(0,1).getValue(), '#')
        self.assertEqual(board.getField(1,0).getValue(), '#')
        self.assertEqual(board.getField(1,1).getValue(), '#')
        board.floodField(1,0)
        self.assertEqual(board.getField(0,0).getValue(), '#')
        self.assertEqual(board.getField(0,1).getValue(), '#')
        self.assertEqual(board.getField(1,0).getValue(), 'o')
        self.assertEqual(board.getField(1,1).getValue(), '#')
        board.floodField(1,0)
        self.assertEqual(board.getField(0,0).getValue(), '#')
        self.assertEqual(board.getField(0,1).getValue(), '#')
        self.assertEqual(board.getField(1,0).getValue(), '.')
        self.assertEqual(board.getField(1,1).getValue(), '#')
        board.floodField(1,0)
        self.assertEqual(board.getField(0,0).getValue(), '#')
        self.assertEqual(board.getField(0,1).getValue(), '#')
        self.assertEqual(board.getField(1,0).getValue(), '.')
        self.assertEqual(board.getField(1,1).getValue(), '#')

    def test_gameBoardCalcFloodCount(self):
        board = gameBoard.gameBoard(3,3)
        self.assertEqual(board.calcFloodCount(board.getField(1,1)),0)
        #felder befuellen
        board.getField(1,0).setValue('o')
        board.getField(0,1).setValue('o')
        board.getField(1,2).setValue('o')
        board.getField(2,1).setValue('.')
        #calc auf innenliegendes
        self.assertEqual(board.calcFloodCount(board.getField(1,1)),3)
        #calc auf am randliegendes
        self.assertEqual(board.calcFloodCount(board.getField(0,2)),2)
        self.assertEqual(board.calcFloodCount(board.getField(2,2)),1)
        self.assertEqual(board.calcFloodCount(board.getField(0,1)),1)

    def test_gameBoardUpdateFloodCount(self):
        board = gameBoard.gameBoard(3,3)
        board.updateFloodCount()
        self.assertEqual(board.getField(1,1).getFloodCount(),0)
        #felder befuellen
        board.getField(1,0).setValue('o')
        board.getField(0,1).setValue('o')
        board.getField(1,2).setValue('o')
        board.getField(2,1).setValue('.')
        board.updateFloodCount()
        #calc auf innenliegendes
        self.assertEqual(board.getField(1,1).getFloodCount(),3)
        #calc auf am randliegendes
        self.assertEqual(board.getField(0,2).getFloodCount(),2)
        self.assertEqual(board.getField(2,2).getFloodCount(),1)
        self.assertEqual(board.getField(0,1).getFloodCount(),1)

    def test_gameBoardFloodFieldUpdatesFloodCount(self):
        board = gameBoard.gameBoard(3,3)
        board.updateFloodCount()
        self.assertEqual(board.getField(1,1).getFloodCount(),0)
        #felder befuellen
        board.floodField(1,0)
        board.floodField(0,1)
        board.floodField(1,2)
        board.floodField(2,1)
        board.floodField(2,1)
        #calc auf innenliegendes
        self.assertEqual(board.getField(1,1).getFloodCount(),3)
        #calc auf am randliegendes
        self.assertEqual(board.getField(0,2).getFloodCount(),2)
        self.assertEqual(board.getField(2,2).getFloodCount(),1)
        self.assertEqual(board.getField(0,1).getFloodCount(),1)

    def test_gameBoardIsValidField(self):
        board = gameBoard.gameBoard(3,3)
        self.assertFalse(board.isValidField((-1,-1)))
        self.assertFalse(board.isValidField((0,-1)))
        self.assertFalse(board.isValidField((1,-1)))
        self.assertFalse(board.isValidField((2,-1)))
        self.assertFalse(board.isValidField((3,-1)))
        self.assertFalse(board.isValidField((-1,0)))
        self.assertTrue(board.isValidField((0,0)))
        self.assertTrue(board.isValidField((1,0)))
        self.assertTrue(board.isValidField((2,0)))
        self.assertFalse(board.isValidField((3,0)))
        self.assertFalse(board.isValidField((-1,1)))
        self.assertTrue(board.isValidField((0,1)))
        self.assertTrue(board.isValidField((1,1)))
        self.assertTrue(board.isValidField((2,1)))
        self.assertFalse(board.isValidField((3,1)))
        self.assertFalse(board.isValidField((-1,2)))
        self.assertTrue(board.isValidField((0,2)))
        self.assertTrue(board.isValidField((1,2)))
        self.assertTrue(board.isValidField((2,2)))
        self.assertFalse(board.isValidField((3,2)))
        self.assertFalse(board.isValidField((-1,3)))
        self.assertFalse(board.isValidField((0,3)))
        self.assertFalse(board.isValidField((1,3)))
        self.assertFalse(board.isValidField((2,3)))
        self.assertFalse(board.isValidField((3,3)))

    def test_gameBoardGetNeighbour(self):
        board = gameBoard.gameBoard(3,3)
        field = board.getField(1,1)
        northField = board.getNeighbour(field,d.direction.NORTH)
        self.assertEquals(northField.getX(),1)
        self.assertEquals(northField.getY(),0)
        nonField = board.getNeighbour(northField,d.direction.NORTH)
        self.assertEquals(nonField, None)
        
        

    ############### GAMEFIELD ###############

    def test_gameFieldGetVales(self):
        field = gameBoard.field(3,2,'#')
        self.assertEqual(field.getValue(), '#')
        self.assertEqual(field.getX(), 3)
        self.assertEqual(field.getY(), 2)
        self.assertEqual(field.getFloodCount(), 0)

    def test_gameFieldFloodCount(self):
        field = gameBoard.field(3,2,'#')
        self.assertEqual(field.getFloodCount(), 0)
        field.setFloodCount(20)
        self.assertEqual(field.getFloodCount(), 20)

    ############### FAKEINPUTREADER ###############

    def test_inputReaderFakeInputReaderReadLines(self):
        lines = ['123','456','789']
        inputReader = reader.fakeInputReader(lines)
        self.assertEqual(inputReader.read(),'123')
        self.assertEqual(inputReader.read(),'456')
        self.assertEqual(inputReader.read(),'789')
        self.assertEqual(inputReader.read(),'IndexError')

    def test_inputReaderCoordinateTextToTuple(self):
        self.assertEqual(reader.coordinateTextToTuple("1,1"),(0,0))
        self.assertEqual(reader.coordinateTextToTuple("27,13"),(26,12))
        

    ############### GAME ###############

    ### Integration Test ###
    def test_runTillEnd(self):
        fooTillEnd = ["GAMEBOARDSTART 8,4",
                      ".oooooo.",
                      "oo####oo",
                      "oo####oo",
                      ".oooooo.",
                      "GAMEBOARDEND",
                      "ROUND 1 3,2",
                      "INCRFLOOD 1",
                      "FLOOD 3,2",
                      "ROUND 2 3,2",
                      "INCRFLOOD 0",
                      "FLOOD 4,4",
                      "ROUND 3 3,2",
                      "END"]
        app = g.game(reader.fakeInputReader(fooTillEnd))
        app.run()
        self.assertTrue(True)

    def test_runTillEndExtended(self):
        inputText = ["GAMEBOARDSTART 38,18",
                     "...ooooo.....oooooooo..........ooooo..",
                     "..oo#ooooo...ooo###ooo...o.oooooooooo.",
                     "oooo##oooo..oo######ooooooooo####ooooo",
                     ".o######ooo.o#####ooooo..oo###oo##ooo.",
                     ".oo######oo.oo###oooo...oo##oo.oo##o..",
                     "ooo######o..o#######ooo.oo##oo..oo##oo",
                     ".ooo##ooo..oo########oooooo##oooo##oo.",
                     ".ooo####oo#####oooo#####oooo##oo##ooo.",
                     "..oooo#######oooo.ooooooooooo###oooo..",
                     "...ooooo####ooo...ooo....oooo##oooo...",
                     ".....ooo###oo.....oooo..oooo##oo......",
                     "....oo####oooooo...oooooooo##oooo.....",
                     "..ooooo########ooooo.oooo###ooooooo...",
                     "oooo######ooo####ooo.oo###oooooo......",
                     "ooo########ooo#####oo####oooo.........",
                     ".ooo########.#####oo#######oooo.......",
                     "..oooo###############oooooooo.........",
                     "....oooooo..oooooo..ooooo.............",
                     "GAMEBOARDEND",
                     "END"]
        #ROUND 1 24,8"
        app = g.game(reader.fakeInputReader(inputText))
        app.run()
        bot = app.getBot()
        bot.setField(app.getGameBoard().getField(24,8))
        nextTurn = bot.calcNextTurn(app.getGameBoard(),0+1)
        self.assertEquals(nextTurn, d.direction.CURRENT)
        bot.makeTurn(app.getGameBoard())

    def test_runTillEndExtendedTwo(self):
        inputText = ["GAMEBOARDSTART 38,18",
                     "...ooooo.....oooooooo..........ooooo..",
                     "..oo#ooooo...ooo###ooo...o.oooooooooo.",
                     "oooo##oooo..oo######ooooooooo####ooooo",
                     ".o######ooo.o#####ooooo..oo###oo##ooo.",
                     ".oo######oo.oo###oooo...oo##oo.oo##o..",
                     "ooo######o..o#######ooo.oo##oo..oo##oo",
                     ".ooo##ooo..oo########oooooo##oooo##oo.",
                     ".ooo####oo#####oooo#####oooo##oo##ooo.",
                     "..oooo#######oooo.ooooooooooo###oooo..",
                     "...ooooo####ooo...ooo....oooo##oooo...",
                     ".....ooo###oo.....oooo..oooo##oo......",
                     "....oo####oooooo...oooooooo##oooo.....",
                     "..ooooo########ooooo.oooo###ooooooo...",
                     "oooo######ooo####ooo.oo###oooooo......",
                     "ooo########ooo#####oo####oooo.........",
                     ".ooo########.#####oo#######oooo.......",
                     "..oooo###############oooooooo.........",
                     "....oooooo..oooooo..ooooo.............",
                     "GAMEBOARDEND",
                     #"ROUND 5 16,7",
                     "END"]
        app = g.game(reader.fakeInputReader(inputText))
        app.run()
        bot = app.getBot()
        bot.setField(app.getGameBoard().getField(15,6))
        self.assertEquals(bot.getField().getValue(),'#')
        nextTurn = bot.calcNextTurn(app.getGameBoard(),0+1)
        self.assertEquals(nextTurn, d.direction.SOUTH)

    def test_runTillEndExtendedTwo(self):
        inputText = ["GAMEBOARDSTART 3,4",
                     "...",
                     "o#.",
                     "###",
                     "###",
                     "GAMEBOARDEND",
                     "END"]
        app = g.game(reader.fakeInputReader(inputText))
        app.run()
        bot = app.getBot()
        bot.setField(app.getGameBoard().getField(1,2))
        self.assertEquals(bot.getField().getValue(),'#')
        nextTurn = bot.calcNextTurn(app.getGameBoard(),0+1)
        self.assertEquals(nextTurn, d.direction.NORTH)
        bot.makeTurn(app.getGameBoard())

    def test_runTillEndExtendedThree(self):
        inputText = ["GAMEBOARDSTART 3,3",
                     "#..",
                     "##.",
                     "#.o",
                     "GAMEBOARDEND",
                     "END"]
        app = g.game(reader.fakeInputReader(inputText))
        app.run()
        bot = app.getBot()
        bot.setField(app.getGameBoard().getField(1,1))
        self.assertEquals(bot.getField().getValue(),'#')
        #nextTurn = bot.calcNextTurn(app.getGameBoard(),0+1)
        bot.makeTurn(app.getGameBoard())

    def test_runTillEndExtendedFour(self):
        inputText = ["GAMEBOARDSTART 3,3",
                     "...",
                     ".o.",
                     "...",
                     "GAMEBOARDEND",
                     "END"]
        app = g.game(reader.fakeInputReader(inputText))
        app.run()
        bot = app.getBot()
        bot.setField(app.getGameBoard().getField(1,1))
        self.assertEquals(bot.getField().getValue(),'o')
        nextTurn = bot.calcNextTurn(app.getGameBoard(),0+1)
        bot.makeTurn(app.getGameBoard())

    def test_runTillEndExtendedFour(self):
        print "start"
        inputText = ["GAMEBOARDSTART 3,3",
                     ".o.",
                     "o.o",
                     ".o.",
                     "GAMEBOARDEND",
                     "END"]
        app = g.game(reader.fakeInputReader(inputText))
        app.run()
        bot = app.getBot()
        bot.setField(app.getGameBoard().getField(1,2))
        self.assertEquals(bot.getField().getValue(),'o')
        nextTurn = bot.calcNextTurn(app.getGameBoard(),0+1)
        self.assertEquals(nextTurn, d.direction.CURRENT)
        bot.makeTurn(app.getGameBoard())
        

    def test_gameReportRound(self):
        test = ["GAMEBOARDSTART 3,3","###", "###", "###", "GAMEBOARDEND", "END"]
        app = g.game(reader.fakeInputReader(test))
        app.run()
        r = gameRound.gameRound()
        self.assertEqual(r.getRound(),1)
        bot = gameBot.gameBot()
        self.assertEquals(bot.getField().getX(),0)
        self.assertEquals(bot.getField().getY(),0)
        inputText = "ROUND 3 3,1"
        app.reportRound(inputText,r,bot)
        self.assertEqual(r.getRound(),3)
        self.assertEquals(bot.getField().getX(),2)
        self.assertEquals(bot.getField().getY(),0)

    def test_gameFlood(self):
        testBoard = ["GAMEBOARDSTART 1,1","#", "GAMEBOARDEND", "END"]
        app = g.game(reader.fakeInputReader(testBoard))
        app.run()
        self.assertEqual(app.getGameBoard().getField(0,0).getValue(),"#")
        app.floodField("FLOOD 0,0")
        self.assertEqual(app.getGameBoard().getField(0,0).getValue(),"o")
        app.floodField("FLOOD 0,0")
        self.assertEqual(app.getGameBoard().getField(0,0).getValue(),".")
        app.floodField("FLOOD 0,0")
        self.assertEqual(app.getGameBoard().getField(0,0).getValue(),".")

    def test_gameIncrFlood(self):
        test = []
        app = g.game(reader.fakeInputReader(test))
        self.assertEquals(app.getFlood(),0)
        app.incrFlood('INCRFLOOD 3')
        self.assertEquals(app.getFlood(),3)
        app.incrFlood('INCRFLOOD 0')
        self.assertEquals(app.getFlood(),3)
        app.incrFlood('INCRFLOOD 1')
        self.assertEquals(app.getFlood(),4)

    def test_gameReadGameBoard(self):
        testBoard = ["oxf", "jlk", "GAMEBOARDEND", "END"]
        app = g.game(reader.fakeInputReader(testBoard))
        board = app.readGameBoard("GAMEBOARDSTART 3,2")
        self.assertEqual(board.getField(0,0).getValue(),"o")
        self.assertEqual(board.getField(0,1).getValue(),"j")
        self.assertEqual(board.getField(1,0).getValue(),"x")
        self.assertEqual(board.getField(1,1).getValue(),"l")
        self.assertEqual(board.getField(2,0).getValue(),"f")
        self.assertEqual(board.getField(2,1).getValue(),"k")

if __name__ == "__main__":
    unittest.main()
