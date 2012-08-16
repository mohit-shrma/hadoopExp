#!/usr/bin/env python
""" produce for each tuple key-value pair of form (b, (R,a)) or (b, (S,c))
for relations R(a, b) and S(b, c) """

import sys
from RelationConsts import RelationConsts


""" depending on the relation generate appropriate key-value pair """
def genKeyVal(cols, separator):
    if cols[RelationConsts.RELATION_NAME_COL]\
            == RelationConsts.FIRST_RELATION_NAME:
        #from first relation
        key = cols[RelationConsts.FIRST_REL_JOIN_COL]
        del cols[RelationConsts.FIRST_REL_JOIN_COL]
        value = ','.join(cols)
    else:
        #from second relation
        key = cols[RelationConsts.SECOND_REL_JOIN_COL]
        del cols[RelationConsts.SECOND_REL_JOIN_COL]
        value = ','.join(cols)
    return key + separator + value


""" parse input from stdin and yield a generator of key value pair"""    
def readInput(file, separator):
    for line in file:
        line = line.strip()
        cols = line.split(',')
        yield genKeyVal(cols, separator)

        
def main(separator = '\t'):

    #input comes from stdin
    data = readInput(sys.stdin, separator)

    #file = open(sys.argv[1], 'r')
    #data = readInput(file, separator)

    for keyVal in data:
        print keyVal

if __name__ == '__main__':
    main()

