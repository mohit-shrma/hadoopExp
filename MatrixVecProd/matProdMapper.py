#!/usr/bin/env python
"""  take each block of matrix and produce ( rowNum/node, blockProdSum) """

import sys
from MapIpSeparators import MapIpSeparators


""" return key-value pairs of form (node, blockProdSum) """
def mapNodeProd(blockNodeData):
    blockProdSums = []
    (nodeData, prVec) = blockNodeData.split(MapIpSeparators.PR_SEP)
    node, outDeg, outNodes = nodeData.split(MapIpSeparators.NODE_DATA_SEP)
    outNodes = outNodes.split(MapIpSeparators.OUT_NODE_SEP)
    for outNode in outNodes:
        tempProd = 1./float(outDeg) * float(prVec)
        blockProdSums.append((outNode, tempProd))
    return blockProdSums


""" parse input from stdin and return a list of key value pair"""    
def readInputNMap(file):
    mapOp = []
    for line in file:
        line = line.strip()
        blockNodesData = line.split(MapIpSeparators.NODE_SEP)
        for blockNodeData in blockNodesData:
             mapOp += mapNodeProd(blockNodeData)
    return mapOp


""" combine the mapOp for same key, return key-value pair as results"""
def combineMapOp(mapOp, separator):
    combineDict = {}
    combineOp = []
    for (key, val) in mapOp:
        if key in combineDict:
            combineDict[key] += val
        else:
            combineDict[key] = val
    for key, val in combineDict.iteritems():
        combineOp.append(str(key) + separator + str(val))
    return combineOp

            
def main(separator = '\t'):

    #input comes from stdin, perform map function on it as it is read
    mapOp = readInputNMap(sys.stdin)

    #mapIpFile = open(sys.argv[1], 'r')
    #mapOp = readInputNMap(mapIpFile)
        
    #run combiner on map output
    combineOp = combineMapOp(mapOp, separator)

    #print key-value pairs from combiner o/p for reduce task
    for keyVal in combineOp:
        print keyVal

        
if __name__ == '__main__':
    main()
