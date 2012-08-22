#!/usr/bin/env python
""" reads the sparse matrix representation of graph, divide it into blocks
and generate block and vector elements as part of map inputs """

import sys
from SparseMatConsts import SparseMatConsts
from MapIpSeparators import MapIpSeparators

""" return webgraphs adjList {node: (outDegree, [neighbors])} """
def readGraph(matFileName):
    graphAdj = {}
    with open(matFileName, 'r') as matFile:
        header = matFile.readline()
        for line in matFile:
            cols = line.split()
            node = cols[SparseMatConsts.NODE_NAME_COL]
            outDegree = cols[SparseMatConsts.OUT_DEG_COL]
            outNodes = cols[SparseMatConsts.OUT_NODES_COL]
            graphAdj[node] = (outDegree, outNodes)
    return graphAdj



""" return initial vector to multiply for pagerank iteration """
def getInitPRVec(nodes):
    numNodes = len(nodes)
    prVec ={}
    for node in nodes:
        prVec[node] = 1./numNodes
    return prVec



""" data for pair is in form 'src,num,vert$Xa:src,num,vert$Xb'  """
def getBlockDataStr(rowBlock, colBlock, graphAdj, prVec):
    blockDataStr = ''
    for node in colBlock:
        (outDegree, outNodes) = graphAdj[node]
        blockOutNodes = [outNode for outNode in outNodes if outNode in rowBlock]
        if len(blockOutNodes) == 0:
            continue
        blockDataStr += node + MapIpSeparators.NODE_DATA_SEP + outDegree \
                        + MapIpSeparators.NODE_DATA_SEP \
                        + MapIpSeparators.OUT_NODE_SEP.join(blockOutNodes) \
                        + MapIpSeparators.PR_SEP + str(prVec[node]) \
                        + MapIpSeparators.NODE_SEP
    blockDataStr = blockDataStr.strip(MapIpSeparators.NODE_SEP)
    return blockDataStr



""" divide passed transition matrix graph in 2X2  blocks and
 correspondic vec to mult. Assuming dimensions of matrix is evenXeven.
 returns line oriented data in form 'src,num,vert$Xa:src,num,vert$Xb'
 for each block  """
def genMapIp(graphAdj, prVec):

    nodes = graphAdj.keys()
    nodes.sort()
    splitBlocks = []
    blockSize = len(nodes)/2

    #break the matrix in blocks
    for i in range(0, len(nodes), blockSize):
        splitBlocks.append(nodes[i: i+blockSize])

    #generate data for each block pair, for same block too and fliped pairs too
    # data for each pair is in form 'src,num,vert$Xa:src,num,vert$Xb'
    blocksDataStr = []

    #generate for diagonal/sameBlock pair
    for block in splitBlocks:
        blockDataStr = getBlockDataStr(block, block, graphAdj, prVec)
        blocksDataStr.append(blockDataStr)

    #generate for other pairs
    for i in range(len(splitBlocks)):
        for j in range(i+1, len(splitBlocks)):
            rowBlock = splitBlocks[i]
            colBlock = splitBlocks[j]
            blockDataStr = getBlockDataStr(rowBlock, colBlock, graphAdj, prVec)
            blocksDataStr.append(blockDataStr)
            blockDataStr = getBlockDataStr(colBlock, rowBlock, graphAdj, prVec)
            blocksDataStr.append(blockDataStr)
    return blocksDataStr
    

def main():
    if len(sys.argv) >= 3:
        matFileName = sys.argv[1]
        mapIpFileName = sys.argv[2]
        graphAdj = readGraph(matFileName)
        prVec = getInitPRVec(graphAdj.keys())
        mapIp = genMapIp(graphAdj, prVec)
        with open(mapIpFileName, 'w') as mapIpFile:
            for line in mapIp:
                mapIpFile.write(line + '\n')
    else:
        print 'file missing'



if __name__ == '__main__':
    main()
