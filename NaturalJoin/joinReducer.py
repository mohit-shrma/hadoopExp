#!/usr/bin/env python
""" 
receives  key, values in form of (joinCol, "Relation,otherCol")
e.g. (b, "S,c" ) and (b, "R,a") and produces all possible tuples of form
ai,b,ci for b """

import sys
from itertools import groupby
from operator import itemgetter
from RelationConsts import RelationConsts


def readMapperOutput(file, separator='\t'):
    for line in file:
        yield line.strip().split(separator, 1)



def main(separator='\t'):
    #input comes from stdin
    data = readMapperOutput(sys.stdin, separator)
    
    # groupby groups multiple joinCol-Rest of relation pairs by word
    # and creates an iterator that return joinCol and their groups
    # joinCol - column on which joining will happen (key)
    # group - iterator yielding all ["joinCol", "Relation,otherCol"]
    #assuming we are receiving data sorted by key


    for joinCol, group in groupby(data, itemgetter(0)):
        firstRelCols = []
        secondRelCols = []
    
        #generate all pairs for 'joinCol'
        for joinCol, restOfRel in group:
            relation, otherCols = restOfRel.split(',', 1)
            if relation == RelationConsts.FIRST_RELATION_NAME:
                #from first relation
                firstRelCols.append(otherCols)
            else:
                #from second relation
                secondRelCols.append(otherCols)

        #generate every pair from first relation and second relation for joinCol
        for firstRelCol in firstRelCols:
            for secondRelCol in secondRelCols:
                print '%s%s%s%s%s' % (firstRelCol, separator, joinCol,\
                                          separator, secondRelCol)


if __name__ == '__main__':
    main()
