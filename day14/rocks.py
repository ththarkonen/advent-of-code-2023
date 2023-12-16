
import json

moves = {"north": (-1, 0),
         "south": ( 1, 0),
         "west":  ( 0,-1),
         "east":  ( 0, 1)}

load = {"north": lambda inds, nRows, nCols: nRows - inds[0],
        "south": lambda inds, nRows, nCols: inds[0] + 1,
        "west":  lambda inds, nRows, nCols: inds[1] + 1,
        "east":  lambda inds, nRows, nCols: nCols - inds[1]}

def parse( lines ):

    roundRocks = []
    cubeRocks = []

    nRows = len( lines )
    nCols = len( lines[0] ) - 1

    for ii in range( nRows ):
        for jj in range( nCols ):

            rock_ii_jj = lines[ii][jj]
            location_ii_jj = ( ii, jj)

            if rock_ii_jj == "#": cubeRocks.append( location_ii_jj )
            if rock_ii_jj == "O": roundRocks.append( location_ii_jj )

    rockObject = {}
    rockObject["nRows"] = nRows
    rockObject["nCols"] = nCols

    rockObject["roundRocks"] = roundRocks
    rockObject["cubeRocks"] = cubeRocks

    return rockObject

def turn( rocks, direction):

    nRows = rocks["nRows"]
    nCols = rocks["nCols"]

    cubeRocks = rocks["cubeRocks"]
    roundRocks = rocks["roundRocks"]

    rocksMoved = True

    move = moves[ direction ]
    nRoundRocks = len( roundRocks )

    while rocksMoved:
        rocksMoved = False

        for rockIndex in range( nRoundRocks ):

            rock = roundRocks[ rockIndex ]

            nextII = rock[0] + move[0]
            nextJJ = rock[1] + move[1]
            nextPosition = ( nextII, nextJJ)

            validPosition = ( 0 <= nextII ) and ( nextII < nRows )
            validPosition = validPosition and ( 0 <= nextJJ ) and ( nextJJ < nCols )

            if not validPosition: continue
            if nextPosition in roundRocks: continue
            if nextPosition in cubeRocks: continue

            roundRocks[ rockIndex ] = nextPosition
            rocksMoved = True

    rocks["roundRocks"] = roundRocks
    return rocks
            

def computeLoad( rocks, direction):

    nRows = rocks["nRows"]
    nCols = rocks["nCols"]
    roundRocks = rocks["roundRocks"]

    totalLoad = 0

    for rock in roundRocks:
        totalLoad = totalLoad + load[ direction ]( rock, nRows, nCols)

    return totalLoad


def findRepeatingPattern( x ):

    n = len( x )

    for ii in range( n - 1, 0, -1):

        nPattern = n - ii
        startInd = ii - nPattern

        pattern = x[ ii: ]
        patternBefore = x[ startInd:ii]

        if pattern == patternBefore:
            return pattern

    return []


def computeFinalLoad( fileName, cycles):

    file = open( fileName )
    loads = json.load( file )

    pattern = findRepeatingPattern( loads )

    nLoads = len( loads )
    nPattern = len( pattern )

    ind = cycles % nPattern
    shift = nLoads % nPattern
    
    loadAtTotalCyles = pattern[ ind - shift - 1]

    return loadAtTotalCyles

