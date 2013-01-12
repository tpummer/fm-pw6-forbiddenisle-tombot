#!/usr/bin/env python

import os, sys, string
import rawInputReader as r
import game as g

def main(argv):
    app = g.game(r.rawInputReader())
    app.run()

if __name__ == "__main__":
    main(sys.argv[1:])
