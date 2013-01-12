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
