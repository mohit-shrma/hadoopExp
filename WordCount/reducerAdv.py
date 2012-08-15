#!/usr/bin/env python
""" advanced reducer employing use of python mapper and generators """

from itertools import groupby
from operator import itemgetter
import sys


def readMapperOutput(file, separator = '\t'):
    for line in file:
        yield line.strip().split(separator, 1)


def main(separator = '\t'):
    #input from stdin
    data = readMapperOutput(sys.stdin, separator=separator)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   currentWord - string containing a word (the key)
    #   group - iterator yielding all ["<current_word>", "<count>"] items
    for currentWord, group in groupby(data, itemgetter(0)):
        try:
            totalCount = sum(int(count) for currentWord, count in group)
            print '%s%s%d' % (currentWord, separator, totalCount)
        except ValueError:
            #count not number, discard
            pass

if __name__ == '__main__':
    main()
    
