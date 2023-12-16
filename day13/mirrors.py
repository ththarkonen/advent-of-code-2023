
import numpy as np

def parse( lines ):

    patterns = []

    newPattern = True

    for line in lines:

        line = line.replace("\n","")
        nCols = len( line )

        if nCols == 0:
            newPattern = True
            patterns.append( pattern )
            continue

        if newPattern:
            pattern = np.empty(( 0, nCols))
            newPattern = False

        row = np.zeros(( 1, nCols))

        for ii, character in enumerate( line ):
            if character == "#": row[0,ii] = 1

        pattern = np.vstack(( pattern, row))
        
    patterns.append( pattern )
    return patterns


def computeReflectionIndex( pattern, mode = "clean"):

    nCols = pattern.shape[1]

    for ii in range( 1, nCols):

        leftPattern = pattern[ :, :ii]
        rightPattern = pattern[ :, ii:]

        nColsLeft = leftPattern.shape[1]
        nColsRight = rightPattern.shape[1]

        nColsII = min( nColsLeft, nColsRight)

        leftPattern = np.fliplr( leftPattern )
        leftPattern = leftPattern[ :, :nColsII]
        rightPattern = rightPattern[ :, :nColsII]

        if mode == "clean":
            isMirror = ~np.any( rightPattern != leftPattern )
        else:
            isMirror = sum( rightPattern.flatten() != leftPattern.flatten() )
            isMirror = isMirror == 1

        if isMirror: return ii

    return 0


def computeReflections( patterns, mode, cleanMode = "clean"):

    locationInds = []

    for pattern in patterns:

        if mode == "horizontal": pattern = pattern.transpose()

        reflectionIndex = computeReflectionIndex( pattern, cleanMode)
        locationInds.append( reflectionIndex )

    return locationInds


