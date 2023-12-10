
import pipelib

file = open("./day10/data.txt")
lines = file.readlines()

startNode, pipes = pipelib.parsePipes( lines )
path = pipelib.traversePipes( startNode, pipes)

innerBoundaries = pipelib.computeInnerBoundaries( path )
containedPixels = pipelib.computeInnerPixels( path, innerBoundaries)

pathLength = 0.5 * len( path )
pathLength = int( pathLength )

nContainedPixels = len( containedPixels )

print( pathLength )
print( nContainedPixels )