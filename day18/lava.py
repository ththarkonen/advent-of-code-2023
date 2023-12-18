
digMoves = {"R": ( 0, 1), "D": ( 1, 0), "U": ( -1, 0), "L": ( 0, -1)}
digDirectionMap = { "0": "R", "1": "D", "2": "L", "3": "U"}

def parse( lines ):

    trenchNodes = {}

    currentII = 0
    currentJJ = 0
    currentPosition = ( currentII, currentJJ)

    node = {}
    node["position"] = currentPosition

    trenchNodes = [ node ]
    nSpots = 1

    for line in lines:

        line = line.replace("\n", "")
        line = line.replace("(", "")
        line = line.replace(")", "")

        digInfo = line.split()
        digDirection = digInfo[0]
        nMoves = int( digInfo[1] )

        digMove = digMoves[ digDirection ]

        for _ in range( nMoves ):

            nextII = currentII + digMove[0]
            nextJJ = currentJJ + digMove[1]
            nextPosition = ( nextII, nextJJ)

            node = {}
            node["position"] = nextPosition

            trenchNodes.append( node )
            nSpots = nSpots + 1

            currentII = nextII
            currentJJ = nextJJ

    return trenchNodes, nSpots

def parseHex( lines ):

    trenchNodes = {}

    currentII = 0
    currentJJ = 0
    currentPosition = ( currentII, currentJJ)

    node = {}
    node["position"] = currentPosition

    trenchNodes = [ node ]
    nSpots = 1

    for line in lines:

        line = line.replace("\n", "")
        line = line.replace("(", "")
        line = line.replace(")", "")

        digInfo = line.split()
        hexCode = digInfo[2]

        nMoves = int( hexCode[1:6], 16)
        digMove = digMoves[ digDirectionMap[ hexCode[-1] ] ]

        nextII = currentII + nMoves * digMove[0]
        nextJJ = currentJJ + nMoves * digMove[1]
        nextPosition = ( nextII, nextJJ)

        node = {}
        node["position"] = nextPosition

        trenchNodes.append( node )
        nSpots = nSpots + nMoves

        currentII = nextII
        currentJJ = nextJJ

    return trenchNodes, nSpots

def calculateArea( trench, nSpots):

    nNodes = len( trench )
    area = nSpots + 1
    
    for nodeInd, node in enumerate( trench ):
        
        if nodeInd == nNodes - 1: nodeInd = 0

        nextNode = trench[ nodeInd + 1]

        dx = nextNode["position"][0] - node["position"][0]
        dy = nextNode["position"][1] + node["position"][1]

        area = area + dx * dy

    area = 0.5 * abs( area )
    area = int( area )

    return area
