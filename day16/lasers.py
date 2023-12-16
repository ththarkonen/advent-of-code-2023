
def parseComponents( lines ):

    nRows = len( lines )
    nCols = len( lines[0] ) - 1

    components = {}

    for ii in range( nRows ):
        for jj in range( nCols ):

            c_ii_jj = lines[ii][jj]

            if c_ii_jj == ".": continue

            position = ( ii, jj)

            component = {}
            component["type"] = c_ii_jj
            component["position"] = position

            components[ position ] = component

    return components, nRows, nCols


def modifyLaserDirection( laserDirection, component):

    if component["type"] == "\\":
        
        laserNewII = laserDirection[1]
        laserNewJJ = laserDirection[0]

        laserDirection = [( laserNewII, laserNewJJ)]
        return laserDirection

    if component["type"] == "/":
        
        laserNewII = -laserDirection[1]
        laserNewJJ = -laserDirection[0]

        laserDirection = [( laserNewII, laserNewJJ)]
        return laserDirection

    if component["type"] == "|":
        if laserDirection[0] == 0:
            laserDirection = [( 1, 0), ( -1, 0)]
            return laserDirection

    if component["type"] == "-":
        if laserDirection[1] == 0:
            laserDirection = [( 0, 1), ( 0, -1)]
            return laserDirection
    
    return [laserDirection]
    

def trace( components, nRows, nCols, start, startDirection):

    nextLasers = [ start ]
    nextLaserDirections = [ startDirection ]

    energizedLocations = [(0,0)]
    energizedData = [(0,0,0,1)]
    newLocations = True

    while newLocations:

        lasers = nextLasers
        laserDirections = nextLaserDirections

        nextLasers = []
        nextLaserDirections = []
        newLocations = False

        for laserIndex, laser in enumerate( lasers ):

            laserDirection = laserDirections[ laserIndex ]

            if laser in components:

                component = components[ laser ]
                nextDirections = modifyLaserDirection( laserDirection, component)
            else:
                nextDirections = [laserDirection]

            for dir in nextDirections:

                nextII = laser[0] + dir[0]
                nextJJ = laser[1] + dir[1]
                nextLocation = ( nextII, nextJJ)
                nextData = ( nextII, nextJJ, dir[0], dir[1])

                validPoint = ( 0 <= nextII ) and ( nextII < nRows )
                validPoint = validPoint and ( 0 <= nextJJ ) and ( nextJJ < nCols )

                if not validPoint: continue
                if nextData in energizedData: continue

                energizedData.append( nextData )
                if nextLocation not in energizedLocations: energizedLocations.append( nextLocation )

                nextLasers.append( nextLocation )
                nextLaserDirections.append( dir )
                newLocations = True

    return len( energizedLocations )





