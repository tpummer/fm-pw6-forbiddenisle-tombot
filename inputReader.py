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
