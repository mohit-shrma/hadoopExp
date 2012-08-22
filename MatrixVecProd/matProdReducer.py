#!/usr/bin/env python

""" combine blocks product received to form page rank vector """

from itertools import groupby
from operator import itemgetter
import sys


def readMapperOutput(file, separator='\t'):
    for line in file:
        yield line.strip().split(separator, 1)

        

def main(separator='\t'):


    
    #input comes from stdin
    data = readMapperOutput(sys.stdin, separator)

    #mapOpFile = open(sys.argv[1], 'r')
    #data = readMapperOutput(mapOpFile, separator)
    
    # groupby groups multiple Node-value pairs by Node,
    # and creates an iterator that returns consecutive keys and their group:
    #   currentNode - string containing a node (the key)
    #   group - iterator yielding all ["<current_node>", "<value>"] items
    for currentNode, group in groupby(data, itemgetter(0)):
        try:
            rank = sum(float(value) for currentNode, value in group)
            print '%s%s%f' % (currentNode, separator, rank)
        except ValueError:
            #value not number, discard
            pass

        

if __name__ == '__main__':
    main()
