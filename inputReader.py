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

class rawInputReader(object):

    ## NOUNITTEST: there's only a raw_input in here
    def read(self):
        return raw_input()

class fakeInputReader(object):
    def __init__(self, input):
        self.linecount = 0
        self.lines = input

    def read(self):
        try:
            result = self.lines[self.linecount]
        except IndexError:
            result = 'IndexError'
            
        self.linecount = self.linecount + 1
        return result

        
def coordinateTextToTuple(inputCoordinates):
    coordinates = inputCoordinates.split(',')
    for i in range(len(coordinates)):
        coordinates[i] = int(coordinates[i]) - 1
    return (coordinates[0], coordinates[1])
