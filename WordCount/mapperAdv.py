#!/usr/bin/env python
""" advanced mapper employing use of python mapper and generators """

import sys

def readInput(file):
    for line in file:
        #split line into words
        yield line.split()

def main(separator='\t'):
    #input comes from stdin
    data = readInput(sys.stdin)
    for words in data:
        #write results to stdout, will be input to reducer
        #tab delimited: trivial word count is 1
        for word in words:
            print '%s%s%s' % (word, separator, 1)

if __name__ == '__main__':
    main()
