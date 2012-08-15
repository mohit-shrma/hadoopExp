#!/usr/bin/env python
from operator import itemgetter
import sys

""" read results from mapper and sum the words to final count as output  """

currentWord = None
currentCount = 0
word = None

for line in sys.stdin:
    line = line.strip()

    #parse the input from mapper word'\t'1
    word, count = line.split('\t', 1)

    #convert count to int
    try:
        count = int(count)
    except ValueError:
        #count was not number so silently ignore it
        continue

    #assuming hadoop sends map output by key-sorted
    if currentWord == word:
        #word received currently is same as current word
        currentCount += count
    else:
        #word received is different from current word
        if currentWord:
            #write result to stdout
            print '%s\t%s' % (currentWord, currentCount)

        #reinit currentWord, currentCount
        currentWord = word
        currentCount = count

#output last word
if currentWord == word:
    print '%s\t%s' % (currentWord, currentCount)

        
