#!/usr/bin/env python

import os, sys, string
import inputReader as reader
import game as g

def main(argv):
    app = g.game(reader.rawInputReader())
    app.run()

if __name__ == "__main__":
    main(sys.argv[1:])
