#!/usr/bin/env python
import sys

""" reads input from STDIN and split it into words
 and output them as (word,1) for each word"""

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        #write results to stdout, this will be input to reducer.py
        print '%s\t%s' % (word, 1)

