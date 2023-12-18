
import numpy as np

directions = [ ( 0, 1), ( 1, 0), ( -1, 0), ( 0, -1)]

def parseHeatLossMap( lines ):

    nRows = len( lines )
    nCols = len( lines[0] ) - 1

    dims = ( nRows, nCols)
    heatLossMap = np.zeros( dims ).astype( np.uint8 )

    for ii in range( nRows ):
        for jj in range( nCols ):
            heatLossMap[ ii, jj] = int( lines[ii][jj] )

    return heatLossMap

def optimizeHeatLoss( heatLossMap, lowerTurnLimit, upperMoveLimit):

    nRows = heatLossMap.shape[0]
    nCols = heatLossMap.shape[1]

    targetLocation = ( nRows - 1, nCols - 1)

    nextPaths = [ ( 0, 0, 1, 0, 1, 0), ( 0, 0, 0, 1, 1, 0)]
    nextPathLocations = [ [(0,0)], [(0,0)]]
    newLocations = True

    heatLosses = {}
    dims = ( nRows, nCols)
    heatLossesMatrix = np.full( dims, np.inf)

    optimalHeatLoss = np.inf

    while newLocations:

        paths = nextPaths
        pathLocations = nextPathLocations

        nextPaths = []
        nextPathLocations = []
        newLocations = False

        for pathIndex, path in enumerate( paths ):

            currentII = path[0]
            currentJJ = path[1]

            currentLocation = ( currentII, currentJJ)
            previousLocations = pathLocations[ pathIndex ].copy()

            if currentLocation == targetLocation:
                continue

            straigtMoveDirII = path[2]
            straigtMoveDirJJ = path[3]

            for dir in directions:

                straigtMoveCount = path[4]

                dirII = dir[0]
                dirJJ = dir[1]

                if straigtMoveCount < lowerTurnLimit:
                    if dirII != straigtMoveDirII or dirJJ != straigtMoveDirJJ:
                        continue

                if dirII == -straigtMoveDirII and dirJJ == -straigtMoveDirJJ: continue

                if dirII == straigtMoveDirII and dirJJ == straigtMoveDirJJ:
                    if straigtMoveCount >= upperMoveLimit: continue
                    straigtMoveCount = straigtMoveCount + 1
                else:
                    straigtMoveCount = 1

                nextII = path[0] + dirII
                nextJJ = path[1] + dirJJ

                nextLocation = ( nextII, nextJJ)
                nextState = ( nextII, nextJJ, dirII, dirJJ, straigtMoveCount)

                currentLoss = path[-1]
                forcedMovement = max( 0, lowerTurnLimit - straigtMoveCount + 1)

                nextForcedII = forcedMovement * dirII + path[0]
                nextForcedJJ = forcedMovement * dirJJ + path[1]

                validPoint = ( 0 <= nextII ) and ( nextII < nRows )
                validPoint = validPoint and ( 0 <= nextJJ ) and ( nextJJ < nCols )
                validPoint = validPoint and ( 0 <= nextForcedII ) and ( nextForcedII < nRows )
                validPoint = validPoint and ( 0 <= nextForcedJJ ) and ( nextForcedJJ < nCols )
                validPoint = validPoint and straigtMoveCount <= upperMoveLimit

                if not validPoint: continue
                nextLoss = currentLoss + heatLossMap[ nextII, nextJJ]

                if heatLossesMatrix[ nextII, nextJJ] > nextLoss:
                    heatLossesMatrix[ nextII, nextJJ] = nextLoss

                nextState = ( nextII, nextJJ, dirII, dirJJ, straigtMoveCount)

                if nextState in heatLosses:
                    if heatLosses[ nextState ] > nextLoss:
                        heatLosses[ nextState ] = nextLoss
                    else:
                        continue
                else:
                    heatLosses[ nextState ] = nextLoss

                if nextLocation == targetLocation:
                    if nextLoss < optimalHeatLoss: optimalHeatLoss = nextLoss
                    continue

                if nextLocation in previousLocations: continue
                previousLocations.append( nextLocation )

                nextPath = ( nextII, nextJJ, dirII, dirJJ, straigtMoveCount, nextLoss)

                nextPaths.append( nextPath )
                nextPathLocations.append( previousLocations.copy() )

                newLocations = True

        tempNextPaths = []
        tempNextLocations = []
        tempChecked = []

        for pathIndex, nextPath in enumerate( nextPaths ):

            ii = nextPath[0]
            jj = nextPath[1]
            dirII = nextPath[2]
            dirJJ = nextPath[3]
            kk = nextPath[4]

            currentState = ( ii, jj, dirII, dirJJ, kk)
            if currentState in tempChecked: continue

            currentLoss = nextPath[-1]

            if currentLoss <= heatLosses[ currentState ]:

                tempChecked.append( currentState )
                
                tempNextPaths.append( nextPath )
                tempNextLocations.append( nextPathLocations[pathIndex] )

        nextPaths = tempNextPaths
        nextPathLocations = tempNextLocations

        print( len( paths ), optimalHeatLoss)

    return optimalHeatLoss