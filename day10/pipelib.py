
import math
import numpy as np

directions = {"|": [( 1, 0), (-1, 0)],
              "-": [( 0, 1), ( 0,-1)],
              "L": [( 0, 1), (-1, 0)],
              "J": [( 0,-1), (-1, 0)],
              "7": [( 0,-1), ( 1, 0)],
              "F": [( 0, 1), ( 1, 0)]}

areaDirections = [( 0, 1), ( 0, -1), ( 1, 0), (-1, 0)]

def rotationMatrix( angle ):

    cosTerm = np.cos( angle )
    sinTerm = np.sin( angle )

    topRow = ( cosTerm, -sinTerm)
    botRow = ( sinTerm, cosTerm)

    R = ( topRow, botRow)
    R = np.array( R ).round()

    return R

def parsePipes( lines ):

    pipes = {}
    startNode = {}
    startNode["connections"] = []

    startingLocation = ""

    nRows = len( lines )
    nCols = len( lines[0] ) - 1

    for ii in range( nRows ):

        line_ii = lines[ii].replace("\n","")

        for jj in range( nCols ):

            char_ii_jj = line_ii[jj]

            if char_ii_jj == ".": continue
            if char_ii_jj == "S":
                startingLocation = ( ii, jj)
                continue

            dirs_ii_jj = directions[ char_ii_jj ]
            pipe_ii_jj = {}
            pipe_ii_jj["type"] = char_ii_jj
            pipe_ii_jj["location"] = ( ii, jj)
            pipe_ii_jj["connections"] = []

            for dir in dirs_ii_jj:

                nextII = ii + dir[0]
                nextJJ = jj + dir[1]
                connection_ii_jj = ( nextII, nextJJ)

                pipe_ii_jj["connections"].append( connection_ii_jj )

            pipeLocation = ( ii, jj)
            pipes[ pipeLocation ] = pipe_ii_jj

        for pipe in pipes.values():
            if startingLocation not in pipe["connections"]: continue

            for connection in pipe["connections"]:
                if startingLocation == connection and pipe["location"] not in startNode["connections"]:
                    startNode["connections"].append( pipe["location"] )

        startNode["location"] = startingLocation

    return startNode, pipes

def traversePipes( startNode, pipes):

    startLocation = startNode["location"]
    nextLocation = startNode["connections"][0]

    ignoringStart = True
    path = [ startLocation ]

    while nextLocation != startLocation:

        currentLocation = nextLocation
        path.append( currentLocation )

        nextPipe = pipes[ currentLocation ]
        
        for connection in nextPipe["connections"]:
            if connection not in path or connection == startLocation and not ignoringStart:
                nextLocation = connection

        ignoringStart = False

    return path

def computeRotationAngle( newDirection, handOrientation):

    x0 = newDirection[0]
    y0 = newDirection[1]

    x1 = handOrientation[0]
    y1 = handOrientation[1]

    anglePrevious = math.atan2( x0, y0)
    angleNext = math.atan2( x1, y1)

    rotationAngle = angleNext - anglePrevious
    return rotationAngle + 0.5 * np.pi

def computeInnerBoundaries( path ):

    startingLocation = path[0]

    hand = np.array(( 1, 0)).astype(int)
    boundaries = []

    nPaths = len( path )

    for ii, location in enumerate( path ):

        handII = location[0] + hand[0]
        handJJ = location[1] + hand[1]
        handLocation = ( handII, handJJ)

        validPoint = handLocation not in boundaries
        validPoint = validPoint and handLocation not in path
        validPoint = validPoint and handLocation != startingLocation

        if validPoint: boundaries.append( handLocation )

        locationII = path[ii]

        if ii == nPaths - 1: locationNext = path[0]
        else: locationNext = path[ii + 1]

        directionII = locationNext[0] - locationII[0]
        directionJJ = locationNext[1] - locationII[1]

        directionVector = ( directionII, directionJJ)
        rotation = computeRotationAngle( directionVector, hand)
        R = rotationMatrix( rotation )

        hand = R @ hand
        hand = hand.round()

        handII = location[0] + hand[0]
        handJJ = location[1] + hand[1]
        handLocation = ( handII, handJJ)

        validPoint = handLocation not in boundaries
        validPoint = validPoint and handLocation not in path
        validPoint = validPoint and handLocation != startingLocation

        if validPoint: boundaries.append( handLocation )

    return boundaries

def computeInnerPixels( path, pixels):

    innerPixels = pixels.copy()

    newPixels = pixels.copy()
    addingNewPixels = True

    while addingNewPixels:

        addingNewPixels = False
        previousPixels = newPixels
        newPixels = []

        for pixel in previousPixels:
            for dir in areaDirections:

                nextII = pixel[0] + dir[0]
                nextJJ = pixel[1] + dir[1]

                nextPixel = ( nextII, nextJJ)

                if nextPixel in path: continue
                if nextPixel in innerPixels: continue
                if nextPixel in newPixels: continue

                newPixels.append( nextPixel )
                addingNewPixels = True

        innerPixels = innerPixels + newPixels

    return innerPixels


